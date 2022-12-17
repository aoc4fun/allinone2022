import { readLinesFromFile } from '../../common/fileUtil'
import { parseInstruction } from './instructionParser'

export interface Instruction {
  quantity: number
  from: number
  to: number
}

function parseStackDrawingLine(line: string): Map<number, string> {
  const splitted = line.split('[')

  const firstOffSet = Math.trunc(splitted[0].length / 4)

  const stacks = new Map()

  for (let i = 0; i < line.length - 1; i += 4) {
    if (line[i] === '[') {
      const position = Math.trunc(i / 4) + 1
      stacks.set(position, line[i + 1])
    }
  }

  return stacks
}

function addElementToStacks(
  stacks: Map<number, Set<string>>,
  element: string,
  position: number
) {
  const stack = stacks.has(position) ? stacks.get(position) : new Set<string>()
  stack.add(element)
  stacks.set(position, stack)
}

function invertSet(set: Set<any>): Array<any> {
  const newArray: any[] = []
  set.forEach((value) => newArray.push(value))
  return newArray.reverse()
}

function executeInstruction(
  stacks: Map<number, Array<string>>,
  instruction: Instruction
) {
  for (let i = 0; i < instruction.quantity; i++) {
    const moved = stacks.get(instruction.from).pop()
    if (moved === undefined) {
      console.error('MOVed is undefined')
      console.log({ instruction })
      ///console.log({ stacks })
    } else {
      stacks.get(instruction.to).push(moved)
    }
  }
}

export function getStacksAndInstructions(filePath: string): {
  stacks: Map<number, Array<string>>
  instructions: Instruction[]
} {
  const lines = readLinesFromFile(filePath)

  const stacks = new Map()
  const instructions: Instruction[] = []
  let lastIndex = 0

  for (const [index, line] of lines.entries()) {
    if (!line.includes('[')) {
      lastIndex = index + 1
      break
    }
    parseStackDrawingLine(line).forEach((value, key) => {
      addElementToStacks(stacks, value, key)
    })
  }
  const invertedStacks = new Map()
  stacks.forEach((value, key) => {
    invertedStacks.set(key, invertSet(value))
  })

  // read lines for instructions
  for (let i = lastIndex + 1; i < lines.length; i++) {
    instructions.push(parseInstruction(lines[i]))
  }

  return { stacks: invertedStacks, instructions }
}

function executeInstructions(
  stacks: Map<number, Array<string>>,
  instructions: Instruction[]
) {
  for (const instruction of instructions) {
    executeInstruction(stacks, instruction)
  }
}

export function getTopCrates(stacks: Map<number, Array<string>>) {
  let message = ''
  for (let i = 1; i <= stacks.size; i++) {
    message += stacks.get(i).pop()
  }
  return message
}

function displayStacks(stacks: Map<number, Array<string>>) {
  console.log('--STACKS--')
  for (let i = 1; i <= stacks.size; i++) {
    console.log(i + ' - ' + stacks.get(i))
  }
  console.log('----------')
}

export function part1(filePath: string): string {
  const { stacks, instructions } = getStacksAndInstructions(filePath)
  console.log('stacks: ', stacks)
  executeInstructions(stacks, instructions)
  const topCrates = getTopCrates(stacks)
  //displayStacks(stacks)
  console.log('--- PART 1 ---')
  console.log('stacks: ', stacks)
  console.log('top crates are: ', topCrates)
  return topCrates
}
