const fs = require('fs')

function createFolder(path) {
  if (!fs.existsSync(path)) {
    fs.mkdirSync(path)
    console.log('📁 Folder created:', path)
    return true
  } else {
    console.error('📁 Folder already exist: ' + path)
    return false
  }
}

function touchFile(path) {
  fs.appendFileSync(path, '')
}

function createAssetFiles(path) {
  touchFile(path + '/example.txt')
  touchFile(path + '/example-answer.txt')
  touchFile(path + '/input.txt')
}

function createAssetFolder(path) {
  if (!createFolder(path)) {
    return false
  }
  const assetPart1Folder = path + '/part1'
  const assetPart2Folder = path + '/part2'
  if (createFolder(assetPart1Folder)) {
    createAssetFiles(assetPart1Folder)
  }
  if (createFolder(assetPart2Folder)) {
    createAssetFiles(assetPart2Folder)
  }
  return true
}

function createSrcFolder(path) {
  if (!createFolder(path)) {
    return false
  }
  const part1Folder = path + '/part1'
  const part2Folder = path + '/part2'
  createFolder(part1Folder)
  createFolder(part2Folder)
  return true
}

function createDayFolder(day) {
  const assetFolder = 'assets/day' + day
  const srcFolder = 'src/day' + day

  if (fs.existsSync(assetFolder) || fs.existsSync(assetFolder)) {
    return false
  }

  createAssetFolder(assetFolder)
  createSrcFolder(srcFolder)

  return true
}

exports.createDayFolder = createDayFolder
