import { readLinesFromFile } from '../../common/fileUtil'
import { getItemPriority } from '../part1/part'

export function part2(filePath: string): number {
  const lines = readLinesFromFile(filePath)

  const groupedBags = Array.from(Array(Math.trunc(lines.length / 3)), () => [])

  let groupIndex = 0

  lines.forEach((bag, index) => {
    groupedBags[groupIndex].push(bag)
    if (index % 3 == 2) {
      groupIndex++
    }
  })

  const badges = groupedBags
    .map((group) => {
      const firstBag = group.shift().split('')
      const reduced = group.reduce((previous, bag) => {
        return previous.filter((value: string) => bag.includes(value))
      }, firstBag)
      // remove duplicates
      return [...new Set(reduced as string[])]
    })
    .flat()

  const score: number = badges.reduce(
    (previous: number, v: string) => previous + getItemPriority(v),
    0
  )

  console.log('groupedBags', groupedBags.length)

  console.log('--- PART 2 ---')
  console.log('GroupeSum priority of badges', score)
  return score
}
