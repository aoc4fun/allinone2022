import { readLinesFromFile } from '../../common/fileUtil'
import { part1 } from './part1'

describe('Day X test', () => {
  it('should work with example data', () => {
    // Arrange
    const expectedAnswer = parseInt(
      readLinesFromFile('assets/day1/part1/example-answer.txt')[0]
    )
    // Act
    const value = part1('assets/day1/part1/example.txt')
    // Assert
    expect(value).toEqual(expectedAnswer)
  })
})
