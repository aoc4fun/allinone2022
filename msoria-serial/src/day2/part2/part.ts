import { readLinesFromFile } from '../../common/fileUtil'
import { getRoundPoints } from '../part1/part'

function getWinningMove(ennemyMove: 'A' | 'B' | 'C') {
  switch (ennemyMove) {
    case 'A':
      return 'Y'
    case 'B':
      return 'Z'
    case 'C':
      return 'X'
  }
}

function getDrawMove(ennemyMove: 'A' | 'B' | 'C') {
  switch (ennemyMove) {
    case 'A':
      return 'X'
    case 'B':
      return 'Y'
    case 'C':
      return 'Z'
  }
}

function getLooseMove(ennemyMove: 'A' | 'B' | 'C') {
  switch (ennemyMove) {
    case 'A':
      return 'Z'
    case 'B':
      return 'X'
    case 'C':
      return 'Y'
  }
}

function getAskedMove(
  ennemyMove: 'A' | 'B' | 'C',
  instruction: 'X' | 'Y' | 'Z'
) {
  switch (instruction) {
    case 'X':
      return getLooseMove(ennemyMove)
    case 'Y':
      return getDrawMove(ennemyMove)
    case 'Z':
      return getWinningMove(ennemyMove)
  }
}

export function part2(filePath: string): number {
  const lines = readLinesFromFile(filePath)

  let totalPoints = 0

  for (const line of lines) {
    const [ennemyMove, instructions] = line.split(' ')

    const askedMove = getAskedMove(
      ennemyMove as 'A' | 'B' | 'C',
      instructions as 'X' | 'Y' | 'Z'
    )

    totalPoints += getRoundPoints(ennemyMove as 'A' | 'B' | 'C', askedMove)
  }

  console.log('--- PART 2 ---')
  console.log('Total Points', totalPoints)

  return totalPoints
}
