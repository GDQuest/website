const gulp = require('gulp')
      htmlmin = require('gulp-htmlmin')
      cssmin = require('gulp-cssmin')
      sass = require('gulp-sass')
      imagemin = require('gulp-imagemin')
      newer = require('gulp-newer');
      ghPages = require('gulp-gh-pages')
      run = require('gulp-run')
      autoprefixer = require('gulp-autoprefixer')


const imgSrc = './_src/img/**/*.{png,jpg,gif,svg}'
const imgDest = './static/img'

const scssWatchFiles = ['./_src/css/**/*.scss']
const scssSrcFile = './_src/css/gdquest.scss'
const cssOutputFolder = './static/css/'


gulp.task('deploy', function () {
  return gulp.src('./public/**/*')
    .pipe(ghPages())
})


gulp.task('watch', function () {
  gulp.watch(scssWatchFiles, ['sass']);
});

gulp.task('sass', function () {
  return gulp.src(scssSrcFile)
    .pipe(sass().on('error', sass.logError))
    .pipe(autoprefixer({
            browsers: ['last 2 versions'],
            cascade: false,
            flexbox: 'no-2009'
        }))
    .pipe(cssmin())
    .pipe(gulp.dest(cssOutputFolder))
})


gulp.task('htmlmin', function () {
  return gulp.src('./public/**/*.html')
    .pipe(htmlmin({
      collapseWhitespace: true
    }))
    .pipe(gulp.dest('public'))
})


gulp.task('imagemin', function () {
  return gulp.src(imgSrc)
    .pipe(newer(imgDest))
    .pipe(imagemin())
    .pipe(gulp.dest(imgDest))
})


gulp.task('default', function () {})