export const getAllNumbers = (str: string) =>
  [...str.matchAll(/\d+/g)].map((n) => Number(n));

// Greatest common divisor of 2 integers
const gcd2 = (a: number, b: number): number => {
  if (!b) return b === 0 ? a : NaN;
  return gcd2(b, a % b);
};

// Least common multiple of 2 integers
const lcm2 = (a: number, b: number) => (a * b) / gcd2(a, b);

// Least common multiple of a list of integers
export const lcm = (array: number[]) => array.reduce((acc, n) => lcm2(n, acc));
