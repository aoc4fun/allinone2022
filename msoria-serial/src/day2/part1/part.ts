import { readLinesFromFile } from '../../common/fileUtil'

function getPointsAgainstA(allyMove: 'X' | 'Y' | 'Z') {
  switch (allyMove) {
    case 'X':
      return 1 + 3
    case 'Y':
      return 2 + 6
    case 'Z':
      return 3 + 0
  }
}

function getPointsAgainstB(allyMove: 'X' | 'Y' | 'Z') {
  switch (allyMove) {
    case 'X':
      return 1 + 0
    case 'Y':
      return 2 + 3
    case 'Z':
      return 3 + 6
  }
}

function getPointsAgainstC(allyMove: 'X' | 'Y' | 'Z') {
  switch (allyMove) {
    case 'X':
      return 1 + 6
    case 'Y':
      return 2 + 0
    case 'Z':
      return 3 + 3
  }
}

export function getRoundPoints(
  ennemyMove: 'A' | 'B' | 'C',
  allyMove: 'X' | 'Y' | 'Z'
) {
  switch (ennemyMove) {
    case 'A':
      return getPointsAgainstA(allyMove)
    case 'B':
      return getPointsAgainstB(allyMove)
    case 'C':
      return getPointsAgainstC(allyMove)
  }
}

export function part1(filePath: string): number {
  const lines = readLinesFromFile(filePath)

  let totalPoints = 0

  for (const line of lines) {
    const [ennemyMove, allyMove] = line.split(' ')

    totalPoints += getRoundPoints(
      ennemyMove as 'A' | 'B' | 'C',
      allyMove as 'X' | 'Y' | 'Z'
    )
  }

  console.log('--- PART 1 ---')
  console.log('Total points: ' + totalPoints)

  return totalPoints
}
