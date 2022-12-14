import { readLinesFromFile } from '../../common/fileUtil'

export function getItemPriority(item: string): number {
  const charCode = item.charCodeAt(0)
  if (charCode >= 'a'.charCodeAt(0) && charCode <= 'z'.charCodeAt(0)) {
    return charCode - 'a'.charCodeAt(0) + 1
  }
  if (charCode >= 'A'.charCodeAt(0) && charCode <= 'Z'.charCodeAt(0)) {
    return charCode - 'A'.charCodeAt(0) + 27
  }
  console.error('ITEM is not in a-zA-Z')
  return 0
}

export function part1(filePath: string): number {
  const lines = readLinesFromFile(filePath)

  let sumOfPriority = 0

  for (const line of lines) {
    const middleIndex = line.length / 2
    const compartment1 = line.slice(0, middleIndex).split('')
    const compartment2 = line.slice(middleIndex, line.length).split('')

    const match = compartment1.find((v) => compartment2.includes(v))
    sumOfPriority += getItemPriority(match)
  }

  console.log('--- PART 1 ---')
  console.log('sumOfPriority: ' + sumOfPriority)

  return sumOfPriority
}
