const gulp = require('gulp')
const jsonModify = require('gulp-json-modify')

function editPackageScripts(day) {
  gulp
    .src('package.json')
    .pipe(
      jsonModify({
        key: 'scripts.start',
        value: 'ts-node src/day' + day + '/index.ts'
      })
    )
    .pipe(gulp.dest('./'))

  gulp
    .src('package.json')
    .pipe(
      jsonModify({
        key: 'scripts.test',
        value: 'jest src/day' + day + '/**/*.spec.ts'
      })
    )
    .pipe(gulp.dest('./'))
}

exports.editPackageScripts = editPackageScripts
