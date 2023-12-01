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
    console.log(line)

    const firstDigit = getFirstDigit(line)
    const lastDigit = getLastDigit(line)

    console.log('first ', firstDigit, 'and last ', lastDigit)

    return parseInt(firstDigit + lastDigit)
}

const total = input.trimEnd().split('\n').reduce((prev, curr) => prev + getSumofFirstAndLastDigits(curr), 0)

console.log(`Result is : ${total}`)