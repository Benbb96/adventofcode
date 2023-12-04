import { getAllNumbers } from "../../utils";

const testInput = `Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11`

const file = Bun.file('input');
const input = await file.text();

const handleLine = (line: string, part2 = false) => {
    const cards = line.split(': ')[1]
    const [winningNumbers, myNumbers] = cards.split(' | ').map(getAllNumbers)

    const totalWinningNumbers = winningNumbers.filter(n => myNumbers.includes(n)).length

    if (part2) {
        return totalWinningNumbers
    }

    return totalWinningNumbers > 0 ? 2 ** (totalWinningNumbers - 1) : 0
}

const total1 = input.trimEnd().split('\n').reduce((prev, curr) => prev + handleLine(curr), 0)
console.log(`Result for part 1 is : ${total1}`)

const totalFoundPerCard = input.trimEnd().split('\n').map((card) => handleLine(card, true))
let totalCards: number[] = Array(totalFoundPerCard.length).fill(1)

for (let i = 0; i < totalFoundPerCard.length; i++) {
    for (let j = 1; j <= totalFoundPerCard[i]; j++) {
        totalCards[i + j] += totalCards[i]
    }
}

const total2 = totalCards.reduce((acc, curr) => acc + curr)
console.log(`Result for part 2 is : ${total2}`)
