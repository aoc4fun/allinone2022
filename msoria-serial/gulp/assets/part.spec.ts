import { readLinesFromFile } from '../../common/fileUtil'
import { part$$PART$$ } from './part'

describe('Day $$DAY$$ part $$PART$$ test', () => {
  it('should work with example data', () => {
    // Arrange
    const expectedAnswer = parseInt(
      readLinesFromFile('assets/day$$DAY$$/example-answer-part$$PART$$.txt')[0]
    )
    // Act
    const value = part$$PART$$('assets/day$$DAY$$/example.txt')
    // Assert
    expect(value).toEqual(expectedAnswer)
  })
})
