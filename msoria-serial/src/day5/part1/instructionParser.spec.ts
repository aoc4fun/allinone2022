import { parseInstruction } from './instructionParser'

describe('Day 5 part 1 instruction parser test', () => {
  it.each([
    // instruction to parse | expected instruction
    ['move 1 from 2 to 1', { quantity: 1, from: 2, to: 1 }],
    ['move 3 from 1 to 3', { quantity: 3, from: 1, to: 3 }],
    ['move 2 from 2 to 1', { quantity: 2, from: 2, to: 1 }],
    ['move 13 from 14 to 16', { quantity: 13, from: 14, to: 16 }]
  ])("should parse instruction '%s'", (instruction, expected) => {
    // Arrange
    // Act
    const parsedInstruction = parseInstruction(instruction)

    // Assert
    expect(parsedInstruction.quantity).toEqual(expected.quantity)
    expect(parsedInstruction.from).toEqual(expected.from)
    expect(parsedInstruction.to).toEqual(expected.to)
  })
})
