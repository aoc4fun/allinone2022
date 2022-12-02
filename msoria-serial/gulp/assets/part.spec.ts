import { readLinesFromFile } from '../../common/fileUtil'
import { part$$PART$$ } from './part'

describe('Day $$DAY$$ test', () => {
  it('should work with example data', () => {
    // Arrange
    const expectedAnswer = parseInt(
      readLinesFromFile('assets/day$$DAY$$/part$$PART$$/example-answer.txt')[0]
    )
    // Act
    const value = part$$PART$$('assets/day$$DAY$$/part$$PART$$/example.txt')
    // Assert
    expect(value).toEqual(expectedAnswer)
  })
})
