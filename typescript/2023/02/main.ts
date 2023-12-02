const testInput = `Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green`

const file = Bun.file('input');
const input = await file.text();

const getMaxRedGreenBlue = (sets: string[]) => {
    let max = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for (const set of sets) {
        const takes = set.split(', ')
        for (const take of takes) {
            const [value, color] = take.split(' ') as [string, 'red' | 'green' | 'blue']
            const val = parseInt(value)
            if (val > max[color]) {
                max[color] = val
            }
        }
    }
    return max
}

const handleLine = (line: string, part2 = false) => {
    const [gameDisplay, actions] = line.split(': ')
    const gameNumber = parseInt(gameDisplay.split(' ').at(-1) as string)
    const sets = actions.split('; ')
    const max = getMaxRedGreenBlue(sets)

    if (part2) {
        return max['red'] * max['green'] * max['blue']
    }

    if (max['red'] <= 12 && max['green'] <= 13 && max['blue'] <= 14) {
        return gameNumber
    }
    return 0
}

const total1 = input.trimEnd().split('\n').reduce((prev, curr) => prev + handleLine(curr), 0)
console.log(`Result for part 1 is : ${total1}`)

const total2 = input.trimEnd().split('\n').reduce((prev, curr) => prev + handleLine(curr, true), 0)
console.log(`Result for part 2 is : ${total2}`)
