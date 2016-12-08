const gulp = require('gulp');
const uncss = require('gulp-uncss');
const htmlmin = require('gulp-htmlmin');
const cssmin = require('gulp-cssmin');
const imagemin = require('gulp-imagemin');

gulp.task('default', function () {

});

gulp.task('minify', function() {
  return gulp.src('public/**/*.html')
    .pipe(htmlmin({collapseWhitespace: true}))
    .pipe(gulp.dest('public'))
});

gulp.task('uncss', function () {
    return gulp.src('D:/Library/Dropbox/Concise_GDquest/dist/concise.css')
        .pipe(uncss({
            html: ['public/**/*.html']
        }))
        .pipe(cssmin())
        .pipe(gulp.dest('D:/Library/Dropbox/GDquest.com/themes/gdquest/static/css/'));
});

gulp.task('picsCompress', function () {
  return gulp.src('public/**/*.{png,jpg,gif,svg}')
  .pipe(imagemin())
  .pipe(gulp.dest('img_compressed'))
})

gulp.task('picsCopy', function () {
  return gulp.src('public/**/*.{png,jpg,gif,svg}')
  .pipe(gulp.dest('img_source'))
})
