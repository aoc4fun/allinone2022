import { readLinesFromFile } from '../../common/fileUtil'

interface Instruction {
  quantity: number
  from: number
  to: number
}

function parseStackDrawingLine(line: string): Map<number, Set<string>> {
  const splitted = line.split('[')

  const firstOffSet = Math.trunc(splitted[0].length / 4)

  const stacks = new Map()

  for (let i = 0; i < splitted.length - 1; i++) {
    const position = firstOffSet + i
    const letter = splitted[i + 1][0]

    const stack = stacks.has(position) ? new Set() : stacks.get(position)
    stack.push(letter)
    stacks.set(position, stack)
  }
  return stacks
}

function getStacksAndInstructions(filePath: string): {
  stacks: Set<string>[]
  instructions: Instruction
} {
  const lines = readLinesFromFile(filePath)

  const stacks = []
  const instructions: Instruction[] = []

  for (const line of lines) {
    if (line === '') {
      break
    }
    const Linestacks = parseStackDrawingLine(line)
  }

  // todo read lines for instructions

  return { stacks, instructions }
}

export function part1(filePath: string): number {
  console.log('--- PART 1 ---')

  return -1
}
