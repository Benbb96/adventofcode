const handlePattern = (pattern: string, part2 = false) => {
    const rows = pattern.split('\n')

    let cols: string[] = Array(rows[0].length).fill('')
    for (const row of rows) {
        for (const [j, char] of [...row].entries()) {
            cols[j] += char
        }
    }

    // Check horizontally
    for (let i = 1; i < rows.length; i++) {
        if (rows[i - 1] === rows[i]) {
            let x = 0
            while (rows[i-1 - x] === rows[i + x]) {
                x++
                if (i-1 - x < 0 || i + x > rows.length -1) {
                    return i * 100
                }
            }
        }
    }

    // Check vertically
    for (let i = 1; i < cols.length; i++) {
        if (cols[i - 1] === cols[i]) {
            let x = 0
            while (cols[i-1 - x] === cols[i + x]) {
                x++
                if (i-1 - x < 0 || i + x > cols.length -1) {
                    return i
                }
            }
        }
    }

    throw new Error("shouldn't happened...")
}

const file = Bun.file('input');
const input = await file.text();
const patterns = input.trimEnd().split('\n\n')

const total1 = patterns.reduce((acc, curr) => acc + handlePattern(curr), 0)
console.log(`Result for part 1 is : ${total1}`)

const total2 = 0
console.log(`Result for part 2 is : ${total2}`)
