import { getCategoriesByElf } from '../part1/part1'

export function part2(filePath: string): number {
  console.log('--- PART 2 ---')

  const { elfCalories } = getCategoriesByElf(filePath)

  elfCalories.sort((a, b) => {
    return b - a
  })

  const threeBestElves = elfCalories[0] + elfCalories[1] + elfCalories[2]

  console.log('3 best elves have ' + threeBestElves + ' calories')

  return threeBestElves
}
