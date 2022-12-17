import {
  getStacksAndInstructions,
  getTopCrates,
  Instruction
} from '../part1/part'

function executeInstructions(
  stacks: Map<number, Array<string>>,
  instructions: Instruction[]
) {
  for (const instruction of instructions) {
    executeInstruction(stacks, instruction)
  }
}

function executeInstruction(
  stacks: Map<number, Array<string>>,
  instruction: Instruction
) {
  const movedCrates = []
  for (let i = 0; i < instruction.quantity; i++) {
    const moved = stacks.get(instruction.from).pop()
    if (moved === undefined) {
      console.error('MOVed is undefined')
      console.log({ instruction })
    } else {
      movedCrates.push(moved)
    }
  }

  movedCrates.reverse()

  for (const crate of movedCrates) {
    stacks.get(instruction.to).push(crate)
  }
}

export function part2(filePath: string): string {
  const { stacks, instructions } = getStacksAndInstructions(filePath)
  console.log('stacks: ', stacks)
  executeInstructions(stacks, instructions)
  const topCrates = getTopCrates(stacks)
  console.log('--- PART 2 ---')

  console.log('stacks: ', stacks)
  console.log('top crates are: ', topCrates)
  return topCrates
}
