const gulp = require('gulp')
      uncss = require('gulp-uncss')
      htmlmin = require('gulp-htmlmin')
      cssmin = require('gulp-cssmin')
      imagemin = require('gulp-imagemin')
      ghPages = require('gulp-gh-pages')
      watch = require('gulp-watch')


gulp.task('deploy', function () {
  return gulp.src('./public/**/*')
    .pipe(ghPages())
})


var cssFolder = 'themes/gdquest/static/css/concise/*.scss'
var cssDistFolder = 'themes/gdquest/css/static'
gulp.task('watch', function () {
  return gulp.src(cssFolder)
    .pipe(watch(cssFolder))
    .pipe()
    .pipe(gulp.dest(cssDistFolder))
})


gulp.task('minify', function () {
  return gulp.src('public/**/*.html')
    .pipe(htmlmin({
      collapseWhitespace: true
    }))
    .pipe(gulp.dest('public'))
})


gulp.task('uncss', function () {
  return gulp.src('D:/Library/Dropbox/GDquest.com/themes/gdquest/static/css/concise/dist/gdquest.css')
    .pipe(uncss({
      html: ['public/**/*.html']
    }))
    .pipe(cssmin())
    .pipe(gulp.dest('D:/Library/Dropbox/GDquest.com/themes/gdquest/static/css/'))
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