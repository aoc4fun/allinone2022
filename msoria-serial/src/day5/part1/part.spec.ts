import { readLinesFromFile } from '../../common/fileUtil'
import { part1 } from './part'

describe('Day 5 part 1 test', () => {
  it('should work with example data', () => {
    // Arrange
    const expectedAnswer = readLinesFromFile(
      'assets/day5/example-answer-part1.txt'
    )[0]

    // Act
    const value = part1('assets/day5/example.txt')
    // Assert
    expect(value).toEqual(expectedAnswer)
  })
})
