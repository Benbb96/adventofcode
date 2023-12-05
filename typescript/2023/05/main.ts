import { getAllNumbers } from "../../utils";


const file = Bun.file('input');
const input = await file.text();
const blocks = input.trimEnd().split('\n\n')
const seeds = getAllNumbers(blocks[0].split(': ')[1])

let mapper = []
for (const block of blocks.slice(1)) {
    const lines = block.split('\n')
    const rules = []
    for (const line of lines.slice(1)) {
        rules.push(getAllNumbers(line))
    }
    mapper.push(rules)
}

const findMinLocationFromSeeds = (seeds: number[], mapper: Array<Array<number>[]>) => {
    let minLocation = Infinity
    for (const seed of seeds) {
        let x = seed
        for (const rules of mapper) {
            for (const [dst, src, range] of rules) {
                if (x >= src && x < src + range) {
                    x = dst + (x - src)
                    break
                }
            }
        }
        if (x < minLocation) {
            minLocation = x
        }
    }
    return minLocation
}

console.log(`Result for part 1 is : ${findMinLocationFromSeeds(seeds, mapper)}`)

let minLocation = Infinity
for (let i = 0; i < seeds.length / 2; i += 2) {
    for (let j = 0; j < seeds[i + 1]; j++) {
        const min = findMinLocationFromSeeds([seeds[i] + j], mapper)
        if (min < minLocation) {
            console.log('better min :', min)
            minLocation = min
        }
    }
}

console.log(`Result for part 2 is : ${minLocation}`)
