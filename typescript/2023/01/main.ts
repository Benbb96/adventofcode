const testInput = `1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet`

const file = Bun.file('input');
const input = await file.text();

const digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

const getFirstDigit = (line: string) => {
    for (let i = 0; i < line.length; i++) {
        const current = line.charAt(i)
        if (digits.includes(current)) {
            return current
        }
    }
    throw new Error('No digit in line')
}

const getLastDigit = (line: string) => {
    for (let i = line.length - 1; i >= 0; i--) {
        const current = line.charAt(i)
        if (digits.includes(current)) {
            return current
        }
    }
    throw new Error('No digit in line')
}

const getSumofFirstAndLastDigits = (line: string) => {
    return Number(getFirstDigit(line) + getLastDigit(line))
}

const total = testInput.trimEnd().split('\n').reduce((prev, curr) => prev + getSumofFirstAndLastDigits(curr), 0)
console.log(`Result for part 1 is : ${total}`)

const testInput2 = `two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`

const easyInput = input.replaceAll('one', 'o1e')
    .replaceAll('two', 't2o')
    .replaceAll('three', 't3e')
    .replaceAll('four', 'f4r')
    .replaceAll('five', 'f5e')
    .replaceAll('six', 's6x')
    .replaceAll('seven', 's7n')
    .replaceAll('eight', 'e8t')
    .replaceAll('nine', 'n9e')

const total2 = easyInput.trimEnd().split('\n').reduce((prev, curr) => prev + getSumofFirstAndLastDigits(curr), 0)
console.log(`Result for part 2 is : ${total2}`)