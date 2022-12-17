import { Instruction } from './part'
export function parseInstruction(instruction: string): Instruction {
  const myRegexp = /move ([0-9]*) from ([0-9]*) to ([0-9]*)/g
  const match = myRegexp.exec(instruction)
  if (!match) {
    console.error('match failed', match)
    console.error('match failed inpout', instruction)
  }
  return {
    quantity: parseInt(match[1]),
    from: parseInt(match[2]),
    to: parseInt(match[3])
  }
}
