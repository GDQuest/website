const gulp = require('gulp')
      htmlmin = require('gulp-htmlmin')
      cssmin = require('gulp-cssmin')
      imagemin = require('gulp-imagemin')
      ghPages = require('gulp-gh-pages')
      watch = require('gulp-watch')
      run = require('gulp-run')


const imgInputFolders = './_src/img/**/*.{png,jpg,gif,svg}'
const imgOutputFolder = './static/img'

const cssSrcFolders = ['./_src/css/concise/**/*.sass']
const cssOutputFolder = './static/css/gdquest.css'


gulp.task('deploy', function () {
  return gulp.src('./public/**/*')
    .pipe(ghPages())
})



gulp.task('watch', function () {
  return watch(cssSrcFolders, function () {
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


gulp.task('cssmin', function () {
  return gulp.src('D:/Library/Dropbox/Gdquest.com/static/css/gdquest.css')
    .pipe(cssmin())
    .pipe(gulp.dest('D:/Library/Dropbox/Gdquest.com/static/css/'))
})


gulp.task('imagemin', function () {
  return gulp.src(imgInputFolders)
    .pipe(imagemin())
    .pipe(gulp.dest(imgOutputFolder))
})


gulp.task('default', function () {})