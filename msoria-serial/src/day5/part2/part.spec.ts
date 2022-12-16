import { readLinesFromFile } from '../../common/fileUtil'
import { part2 } from './part'

describe('Day 5 part 2 test', () => {
  it('should work with example data', () => {
    // Arrange
    const expectedAnswer = parseInt(
      readLinesFromFile('assets/day5/example-answer-part2.txt')[0]
    )
    // Act
    const value = part2('assets/day5/example.txt')
    // Assert
    expect(value).toEqual(expectedAnswer)
  })
})
