const file = Bun.file('input');
const input = await file.text();
const grid = input.trimEnd().split('\n')

const isInGrid = (grid: string[], row: number, col: number) => {
    try {
        if (grid[row][col]) return true
    } catch {
        return false
    }
}
const isSymbol = (grid: string[], row: number, col: number) => !'.0123456789'.includes(grid[row][col])

const partNumbers: number[] = []
const gearsNumbers: {symbolPosition: string, number: number}[] = []
let number = ''
let symbolNearby = false
let symbolPosition = ''
let i = 0
for (const line of grid) {
    let j = 0
    for (const char of line) {
        if (char >= '0' && char <= '9') {
            // Append to current number
            if (number) {
                number += char
            } else {
                number = char
            }

            // Check if symbol in neighbors
            if (!symbolNearby) {
                for (const [x, y] of [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]) {
                    if (isInGrid(grid, i + x, j + y) && isSymbol(grid, i + x, j + y)) {
                        symbolNearby = true
                        if (grid[i + x][j + y] === '*') {
                            symbolPosition = `${i + x}-${j + y}`
                        }
                        break
                    }
                }
            }
        } else {
            // end of number
            if (number) {
                if (symbolNearby) {
                    partNumbers.push(Number(number))
                    if (symbolPosition) {
                        gearsNumbers.push({symbolPosition, number: Number(number)})
                    }
                }
                // reset variables
                number = ''
                symbolNearby = false
                symbolPosition = ''
            }
        }
        j++
    }
    i++
}

const total1 = partNumbers.reduce((acc, curr) => acc + curr, 0)
console.log(`Result for part 1 is : ${total1}`)

const uniqueSymbolPositions = gearsNumbers.reduce(
    (acc, curr) => acc.includes(curr.symbolPosition) ? acc : [...acc, curr.symbolPosition],
    [] as string[]
)
let total2 = 0
for (const pos of uniqueSymbolPositions) {
    const numbers = gearsNumbers.filter(gn => gn.symbolPosition === pos)
    if (numbers.length === 2) {
        total2 += numbers[0].number * numbers[1].number
    }
}

console.log(`Result for part 2 is : ${total2}`)
