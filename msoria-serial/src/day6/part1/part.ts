import { readLinesFromFile } from '../../common/fileUtil'

export function getFirstMarker(signal: string, distinctNumber: number): number {
  const markerBuffer: string[] = []
  let i = 0
  do {
    const marker = signal[i]
    if (markerBuffer.includes(marker)) {
      markerBuffer.splice(0, markerBuffer.findIndex((v) => v === marker) + 1)
    }
    markerBuffer.push('' + marker)
    i++
  } while (markerBuffer.length < distinctNumber && i < signal.length)
  return i
}

export function getSignalFirstMarker(signal: string): number {
  return getFirstMarker(signal, 4)
}

export function part1(filePath: string): number {
  console.log('--- PART 1 ---')

  const lines = readLinesFromFile(filePath)

  const index = getSignalFirstMarker(lines[0])
  console.log('First start-of-packet marker: ', index)

  return index
}
