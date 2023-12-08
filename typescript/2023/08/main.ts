type MatchedLine = {
    source: string,
    right: string,
    left: string
}

const lineRegex = RegExp(/(?<source>[A-Z]{3}) = \((?<left>[A-Z]{3}), (?<right>[A-Z]{3})\)/)

const file = Bun.file('input');
const input = await file.text();

const [rule, maps] = input.trimEnd().split('\n\n')
const mapping = new Map()
for (const line of maps.split('\n')) {
    const {source, left, right} = line.match(lineRegex)?.groups as MatchedLine
    mapping.set(source + 'L', left)
    mapping.set(source + 'R', right)
}

let totalSteps = 0
let currentPosition = 'AAA'

while (currentPosition !== 'ZZZ') {
    const direction = rule.charAt(totalSteps % rule.length)
    console.log(direction)
    currentPosition = mapping.get(currentPosition + direction)
    console.log(currentPosition)
    totalSteps++
}
console.log(`Result for part 1 is : ${totalSteps}`)

// const total2 = lines.reduce((acc, curr) => acc + handleLine(curr, true), 0)
// console.log(`Result for part 2 is : ${total2}`)
