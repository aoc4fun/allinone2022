import { getSignalFirstMarker } from './part'

describe('Day 6 part 1 test', () => {
  it.each([
    // signal | expected first marker
    ['mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7],
    ['bvwbjplbgvbhsrlpgdmjqwftvncz', 5],
    ['nppdvjthqldpwncqszvftbrmjlhg', 6],
    ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10],
    ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11]
  ])("should parse signal '%s'", (signal, expected) => {
    // Arrange signal
    // Act
    const value = getSignalFirstMarker(signal)
    // Assert
    expect(value).toEqual(expected)
  })
})
