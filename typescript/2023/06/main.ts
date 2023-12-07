const file = Bun.file('input');
const input = await file.text();
const lines = input.trimEnd().split('\n')

const mappingValue = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

const getTypeValue = (hand: string[]) => {
    const counter = [...hand.reduce((acc, e) => acc.set(e, (acc.get(e) || 0) + 1), new Map<string, number>()).entries()];
    switch (counter.length) {
        case 1: return 7
        case 2: return counter[0][1] === 4 || counter[1][1] === 4 ? 6 : 5
        case 3: return counter[0][1] === 3 || counter[1][1] === 3 || counter[2][1] === 3 ? 4 : 3
        case 4: return 2
        case 5: return 1
        default: throw new Error('Impossible')
    }
}

// Parse
const hands = lines.map(line => {
    const [hand, bid] = line.split(' ')
    return {hand, bid: Number(bid)}
})

// Sort from worse hand to best hand
const sortedHands = hands.sort((a, b) => {
    const aArray = [...a.hand]
    const bArray = [...b.hand]
    let diff = getTypeValue(aArray) - getTypeValue(bArray)
    if (diff === 0) {
        for (let i = 0; i < 5; i++) {
            const currentAValue = mappingValue[aArray[i] as keyof typeof mappingValue]
            const currentBValue = mappingValue[bArray[i] as keyof typeof mappingValue]
            diff = currentAValue - currentBValue
            if (diff !== 0) break
        }
    }
    return diff
})

// Calculate total
const total1 = sortedHands.reduce((acc, curr, index) => acc + curr.bid * (index + 1), 0)
console.log(`Result for part 1 is : ${total1}`)

// const total2 = lines.reduce((acc, curr) => acc + handleLine(curr, true), 0)
// console.log(`Result for part 2 is : ${total2}`)
