const { src, dest } = require('gulp')
const replace = require('gulp-replace')

function copyPartTemplate(day, part) {
  src(['gulp/assets/part.ts', 'gulp/assets/part.spec.ts'])
    .pipe(replace('$$DAY$$', day))
    .pipe(replace('$$PART$$', part))
    .pipe(dest('src/day' + day + '/part' + part))
}

function copyIndexTemplate(day) {
  src(['gulp/assets/index.ts'])
    .pipe(replace('$$DAY$$', day))
    .pipe(dest('src/day' + day + '/'))
}

function copyTemplates(day) {
  copyPartTemplate(day, 1)
  copyPartTemplate(day, 2)
  copyIndexTemplate(day)
}

exports.copyTemplates = copyTemplates
