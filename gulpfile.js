const gulp = require('gulp')
      htmlmin = require('gulp-htmlmin')
      cssmin = require('gulp-cssmin')
      imagemin = require('gulp-imagemin')
      newer = require('gulp-newer');
      ghPages = require('gulp-gh-pages')
      watch = require('gulp-watch')
      run = require('gulp-run')
      convert = require('sass-convert')


const imgSrc = './_src/img/**/*.{png,jpg,gif,svg}'
const imgDest = './static/img'

const cssSrcFolders = ['./_src/css/**/*.+(sass|scss)']
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
  return run('concisecss compile _src/css/gdquest.scss static/css/gdquest.css').exec()
})


gulp.task('htmlmin', function () {
  return gulp.src('./public/**/*.html')
    .pipe(htmlmin({
      collapseWhitespace: true
    }))
    .pipe(gulp.dest('public'))
})

gulp.task('cssmin', function () {
  return gulp.src('./static/**/*.css')
    .pipe(cssmin())
    .pipe(gulp.dest('./static'))
})



gulp.task('imagemin', function () {
  return gulp.src(imgSrc)
    .pipe(newer(imgDest))
    .pipe(imagemin())
    .pipe(gulp.dest(imgDest))
})


gulp.task('default', function () {})