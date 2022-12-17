import { getMessageFirstMarker } from './part'

describe('Day 6 part 2 test', () => {
  it.each([
    // signal | expected first marker
    ['mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19],
    ['bvwbjplbgvbhsrlpgdmjqwftvncz', 23],
    ['nppdvjthqldpwncqszvftbrmjlhg', 23],
    ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29],
    ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26]
  ])("should parse signal '%s'", (signal, expected) => {
    // Arrange signal
    // Act
    const value = getMessageFirstMarker(signal)
    // Assert
    expect(value).toEqual(expected)
  })
})
