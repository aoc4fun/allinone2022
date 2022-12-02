import { readLinesFromFile } from '../../common/fileUtil'

export function getCategoriesByElf(filePath: string) {
  const lines = readLinesFromFile(filePath)

  const elfCalories = []
  let currentElfCalories = 0
  let bestElf = 0

  for (const line of lines) {
    if (line === '' && currentElfCalories > 0) {
      // update best elf
      if (currentElfCalories > bestElf) {
        bestElf = currentElfCalories
      }
      elfCalories.push(currentElfCalories)
      currentElfCalories = 0
    } else {
      currentElfCalories += parseInt(line)
    }
  }

  return { elfCalories, bestElf }
}

export function part1(filePath: string): number {
  console.log('--- PART 1 ---')

  const { bestElf } = getCategoriesByElf(filePath)

  console.log('Best elf has: ', bestElf)

  return bestElf
}
