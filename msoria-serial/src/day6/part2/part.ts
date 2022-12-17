import { readLinesFromFile } from '../../common/fileUtil'
import { getFirstMarker } from '../part1/part'

export function getMessageFirstMarker(signal: string): number {
  return getFirstMarker(signal, 14)
}

export function part2(filePath: string): number {
  console.log('--- PART 2 ---')

  const lines = readLinesFromFile(filePath)

  const index = getMessageFirstMarker(lines[0])
  console.log('First start-of-message marker: ', index)

  return index
}
