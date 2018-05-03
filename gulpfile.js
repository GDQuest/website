const gulp = require('gulp')
      htmlmin = require('gulp-htmlmin')
      cssmin = require('gulp-cssmin')
      sass = require('gulp-sass')
      imagemin = require('gulp-imagemin')
      imageResize = require('gulp-image-resize');
      rename = require("gulp-rename")
      newer = require('gulp-newer');
      ghPages = require('gulp-gh-pages')
      run = require('gulp-run')
      autoprefixer = require('gulp-autoprefixer')
      plumber = require('gulp-plumber')

const imgSrc = './_src/img/**/*.{png,jpg,gif,svg}'
const bannerSrc = './static/img/**/banner.jpg'
const imgDest = './static/img'

const scssWatchFiles = ['./_src/scss/**/*.scss']
const scssSrcFile = './_src/scss/gdquest.scss'
const cssOutputFolder = './static/css/'


gulp.task('deploy', function () {
  return gulp.src('./public/**/*')
    .pipe(ghPages())
})


gulp.task('watch', function () {
  gulp.watch(scssWatchFiles, ['build-css']);
});

gulp.task('build-css', function () {
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


gulp.task('img', function () {
  return gulp.src(imgSrc)
    .pipe(newer(imgDest))
    .pipe(imagemin())
    .pipe(gulp.dest(imgDest))
})

gulp.task('resize', function() {
  return gulp.src(bannerSrc)
    .pipe(plumber())
    .pipe(imageResize({
      width : 580,
      crop : false,
      upscale : false,
      noProfile: true,
      interlace: true,
      format: 'jpg',
      quality: 1.0,
      sharpen: true
    }))
    .pipe(rename(function(path) {
      path.basename += "-sm"
    }))
    .pipe(gulp.dest(imgDest))
})

gulp.task('thumbs', function() {
  return gulp.src('./static/img/product/**/banner.jpg')
    .pipe(plumber())
    .pipe(imageResize({
      width : 360,
      crop : false,
      upscale : false,
      noProfile: true,
      interlace: true,
      format: 'jpg',
      quality: 1.0,
      sharpen: true
    }))
    .pipe(rename(function(path) {
      path.basename += "-thumb"
    }))
    .pipe(gulp.dest('./static/img/product'))
})
