import { lcm } from "../../utils";

type MatchedLine = {
  source: string;
  right: string;
  left: string;
};

const lineRegex = RegExp(
  /(?<source>[A-Z]{3}) = \((?<left>[A-Z]{3}), (?<right>[A-Z]{3})\)/
);

const file = Bun.file("input");
const input = await file.text();

const [rule, maps] = input.trimEnd().split("\n\n");
const mapping = new Map();
const allSources = [];
for (const line of maps.split("\n")) {
  const { source, left, right } = line.match(lineRegex)?.groups as MatchedLine;
  allSources.push(source);
  mapping.set(source + "L", left);
  mapping.set(source + "R", right);
}

let totalSteps = 0;
let currentPosition = "AAA";

while (currentPosition !== "ZZZ") {
  const direction = rule.charAt(totalSteps % rule.length);
  currentPosition = mapping.get(currentPosition + direction);
  totalSteps++;
}

console.log(`Result for part 1 is : ${totalSteps}`);

const iterationsBeforeEndingZ = [];

for (let node of allSources.filter((s) => s.endsWith("A"))) {
  let i = 0;
  while (!node.endsWith("Z")) {
    const direction = rule.charAt(i % rule.length);
    node = mapping.get(node + direction);
    i++;
  }
  iterationsBeforeEndingZ.push(i);
}

console.log(`Result for part 2 is : ${lcm(iterationsBeforeEndingZ)}`);
