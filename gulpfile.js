const gulp = require('gulp')
      htmlmin = require('gulp-htmlmin')
      cssmin = require('gulp-cssmin')
      sass = require('gulp-sass')
      ghPages = require('gulp-gh-pages')
      autoprefixer = require('gulp-autoprefixer')

const scssWatchFiles = ['./_src/scss/**/*.scss']
const scssSrcFile = './_src/scss/gdquest.scss'
const cssOutputFolder = './static/css/'


gulp.task('watch', function () {
    gulp.watch(scssWatchFiles, ['scss']);
});


gulp.task('scss', function () {
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


gulp.task('deploy', function () {
    return gulp.src('./public/**/*')
        .pipe(ghPages())
})
