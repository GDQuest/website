const gulp = require('gulp')
      uncss = require('gulp-uncss')
      htmlmin = require('gulp-htmlmin')
      cssmin = require('gulp-cssmin')
      imagemin = require('gulp-imagemin')
      ghPages = require('gulp-gh-pages')
      watch = require('gulp-watch')
      run = require('gulp-run')


gulp.task('deploy', function () {
  return gulp.src('./public/**/*')
    .pipe(ghPages())
})


var cssFolders = ['./_src/css/concise/*.scss', './_src/css/concise/modules/*.sass']
var cssDist = './static/css/gdquest.css'

gulp.task('watch', function () {
  return watch(cssFolders, function () {
        gulp.start('build-css')
    })
})

gulp.task('build-css', function () {
  return run('npm run build-css').exec()
})


gulp.task('minify', function () {
  return gulp.src('public/**/*.html')
    .pipe(htmlmin({
      collapseWhitespace: true
    }))
    .pipe(gulp.dest('public'))
})


gulp.task('uncss', function () {
  return gulp.src('D:/Library/Dropbox/Gdquest.com/static/css/gdquest.css')
    .pipe(uncss({
      html: ['public/**/*.html']
    }))
    .pipe(cssmin())
    .pipe(gulp.dest('D:/Library/Dropbox/Gdquest.com/static/css/gdquest.css'))
})


gulp.task('compress', function () {
  return gulp.src('public/**/*.{png,jpg,gif,svg}')
    .pipe(imagemin())
    .pipe(gulp.dest('img_compressed'))
})


gulp.task('picsCopy', function () {
  return gulp.src('public/**/*.{png,jpg,gif,svg}')
    .pipe(gulp.dest('img_source'))
})


gulp.task('default', function () {})