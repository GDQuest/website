const gulp = require('gulp')
      htmlmin = require('gulp-htmlmin')
      ghPages = require('gulp-gh-pages')

gulp.task('htmlmin', function () {
  return gulp.src('./public/**/*.html')
    .pipe(htmlmin({
      collapseWhitespace: true
    }))
    .pipe(gulp.dest('public'))
})

gulp.task('deploy', function () {
    return gulp.src('./public/**/*')
        .pipe(ghPages())
})
