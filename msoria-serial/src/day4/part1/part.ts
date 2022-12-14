import { readLinesFromFile } from '../../common/fileUtil'

export function parseElfSections(elfSection: string) {
  return elfSection.split('-').map((v) => parseInt(v))
}

function isPairInsidePair(sections1: number[], sections2: number[]) {
  return sections1[0] >= sections2[0] && sections1[1] <= sections2[1]
}

function isOnePairInsideOther(
  sections1: number[],
  sections2: number[]
): boolean {
  return (
    isPairInsidePair(sections1, sections2) ||
    isPairInsidePair(sections2, sections1)
  )
}

export function part1(filePath: string): number {
  const lines = readLinesFromFile(filePath)

  let assignmentPairs = 0

  for (const line of lines) {
    const elfsSections = line.split(',')
    const elf1Sections = parseElfSections(elfsSections[0])
    const elf2Sections = parseElfSections(elfsSections[1])
    assignmentPairs += isOnePairInsideOther(elf1Sections, elf2Sections) ? 1 : 0
  }

  console.log('--- PART 1 ---')
  console.log('assignment pairs: ', assignmentPairs)

  return assignmentPairs
}
