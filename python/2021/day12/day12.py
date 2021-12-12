from python.download_input import get_input_content


def first(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == end:
        return [path]

    if start not in graph:
        return []
    paths = []

    for node in graph[start]:
        if start != 'start' and node != 'end' and node.islower():
            if node not in path:
                newpaths = first(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        else:
            newpaths = first(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def path_already_have_two_small(path):
    nodes = set(path)
    for node in nodes:
        if node.islower() and path.count(node) == 2:
            return node
    return


def second(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == end:
        return [path]

    if start not in graph:
        return []
    paths = []

    for node in graph[start]:
        if start != 'start' and node != 'end' and node.islower():
            already_two = path_already_have_two_small(path)
            if already_two and node != already_two and path.count(node) < 1 or not already_two:
                newpaths = second(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        else:
            newpaths = second(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


if __name__ == "__main__":
    content = get_input_content(__file__)

    graph_input = {}
    for line in content:
        a, b = line.split('-')
        if b != 'start':
            if a in graph_input:
                graph_input[a].append(b)
            else:
                graph_input[a] = [b]
        # Graph is biderectional
        if a != 'start':
            if b in graph_input:
                graph_input[b].append(a)
            else:
                graph_input[b] = [a]

    print(f'Le résultat de la première partie est :\n{len(first(graph_input, "start", "end"))}')

    print(f'Le résultat de la deuxième partie est :\n{len(second(graph_input, "start", "end"))}')
