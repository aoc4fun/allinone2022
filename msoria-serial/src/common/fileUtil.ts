import * as FS from 'fs'

export function readLinesFromFile(path: string): Array<string> {
  return FS.readFileSync(path, 'utf-8').replace('\r', '').split('\n')
}
