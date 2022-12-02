import { readLinesFromFile } from '../../common/fileUtil'
import { part1 } from './part'

describe('Day 2 test', () => {
  it('should work with example data', () => {
    // Arrange
    const expectedAnswer = parseInt(
      readLinesFromFile('assets/day2/part1/example-answer.txt')[0]
    )
    // Act
    const value = part1('assets/day2/part1/example.txt')
    // Assert
    expect(value).toEqual(expectedAnswer)
  })
})
