const gulp = require('gulp')
const run = require('gulp-run')
const { copyTemplates } = require('./gulp/scripts/copyTemplates')
const { editPackageScripts } = require('./gulp/scripts/editPackageScripts')
const createDayFolder =
  require('./gulp/scripts/createDayFolder').createDayFolder

const argv = require('minimist')(process.argv.slice(2))

function newDay(cb) {
  const day = argv.day
  if (createDayFolder(day)) {
    copyTemplates(day)
    editPackageScripts(day)
  } else {
    console.error('❌ Creation of day' + day + ' files aborted')
    cb()
    return
  }
  console.log('✅ Creation of day' + day + ' done')
  console.log('🗡 Go crush that challenge !')
  cb()
}

function switchDay(cb) {
  const day = argv.day

  editPackageScripts(day)
  cb()
}

exports.new = newDay
exports.switch = switchDay
