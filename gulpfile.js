const gulp = require('gulp')
      uncss = require('gulp-uncss')
      htmlmin = require('gulp-htmlmin')
      cssmin = require('gulp-cssmin')
      imagemin = require('gulp-imagemin')
      ghPages = require('gulp-gh-pages')


gulp.task('deploy', function(){
  return gulp.src('./public/**/*')
    .pipe(ghPages())
})


gulp.task('default', function () {
})


gulp.task('minify', function() {
  return gulp.src('public/**/*.html')
    .pipe(htmlmin({collapseWhitespace: true}))
    .pipe(gulp.dest('public'))
})


gulp.task('uncss', function () {
    return gulp.src('D:/Library/Dropbox/GDquest.com/themes/gdquest/static/css/concise_gdquest/dist/concise.css')
        .pipe(uncss({
            html: ['public/**/*.html']
        }))
        .pipe(cssmin())
        .pipe(gulp.dest('D:/Library/Dropbox/GDquest.com/themes/gdquest/static/css/'))
})


gulp.task('picsCompress', function () {
  return gulp.src('public/**/*.{png,jpg,gif,svg}')
  .pipe(imagemin())
  .pipe(gulp.dest('img_compressed'))
})


gulp.task('picsCopy', function () {
  return gulp.src('public/**/*.{png,jpg,gif,svg}')
  .pipe(gulp.dest('img_source'))
})
