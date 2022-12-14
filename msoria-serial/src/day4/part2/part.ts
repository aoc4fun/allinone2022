import { readLinesFromFile } from '../../common/fileUtil'
import { parseElfSections } from '../part1/part'

function isIn(n: number, bounds: number[]) {
  return n >= bounds[0] && n <= bounds[1]
}

function hasOverlap(section1: number[], section2: number[]) {
  return (
    isIn(section1[0], section2) ||
    isIn(section1[1], section2) ||
    isIn(section2[0], section1) ||
    isIn(section2[1], section1)
  )
}

export function part2(filePath: string): number {
  const lines = readLinesFromFile(filePath)

  let overlaps = 0

  for (const line of lines) {
    const elfsSections = line.split(',')
    const elf1Sections = parseElfSections(elfsSections[0])
    const elf2Sections = parseElfSections(elfsSections[1])
    overlaps += hasOverlap(elf1Sections, elf2Sections) ? 1 : 0
  }

  console.log('--- PART 2 ---')
  console.log('overlaps: ', overlaps)
  return overlaps
}
