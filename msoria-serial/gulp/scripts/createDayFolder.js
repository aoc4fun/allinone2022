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
  touchFile(path + '/example-answer-part1.txt')
  touchFile(path + '/example-answer-part2.txt')
  touchFile(path + '/input.txt')
}

function createAssetFolder(path) {
  if (!createFolder(path)) {
    return false
  }
  createAssetFiles(path)
  return true
}

function createDayFolder(day) {
  const assetFolder = 'assets/day' + day
  const srcFolder = 'src/day' + day

  if (fs.existsSync(assetFolder) || fs.existsSync(assetFolder)) {
    return false
  }

  createAssetFolder(assetFolder)
  createFolder(srcFolder)

  return true
}

exports.createDayFolder = createDayFolder
