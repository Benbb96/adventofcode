import re

from python.download_input import get_input_content


def first(workflows, parts):
    total = 0
    for part in parts:
        workflow = 'in'
        x = part['x']
        m = part['m']
        a = part['a']
        s = part['s']
        while workflow not in ('A', 'R'):
            rules = workflows[workflow]
            for rule in rules:
                if ':' not in rule:
                    workflow = rule
                    break
                condition, next_workflow = rule.split(':')
                if eval(condition.replace('x', x).replace('m', m).replace('a', a).replace('s', s)):
                    workflow = next_workflow
                    break

        if workflow == 'A':
            total += sum(map(int, part.values()))

    return total


def second(data):
    return 2


if __name__ == "__main__":
    content = get_input_content(__file__, split_by_lines=False)
    test_input = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}'''

    workflows_text, parts_text = content.split('\n\n')
    workflows = {}
    for workflow in workflows_text.split('\n'):
        workflow_name, rest = workflow.split('{')
        rules = rest[:-1].split(',')
        workflows[workflow_name] = rules

    parsing = re.compile(r'\{x=(?P<x>\d+),m=(?P<m>\d+),a=(?P<a>\d+),s=(?P<s>\d+)}')
    parts = []
    for part in parts_text.split('\n'):
        print(part)
        parts.append(re.match(parsing, part).groupdict())

    print(f'Le résultat de la première partie est :\n{first(workflows, parts)}')

    print(f'Le résultat de la deuxième partie est :\n{second(content)}')
