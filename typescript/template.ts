const testInput = ``

const handleLine = (line: string, part2 = false) => {
    console.log(line)
    return 0
}

const file = Bun.file('input');
const input = await file.text();
const lines = input.trimEnd().split('\n')

const total1 = lines.reduce((acc, curr) => acc + handleLine(curr), 0)
console.log(`Result for part 1 is : ${total1}`)

const total2 = lines.reduce((acc, curr) => acc + handleLine(curr, true), 0)
console.log(`Result for part 2 is : ${total2}`)
