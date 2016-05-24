process.chdir('nekmocom/static/nekmocom');
var gulp = require('gulp'),
    compass = require('gulp-compass');
    cleanCSS = require('gulp-clean-css');
    importCSS = require('gulp-import-css');
    replace = require('gulp-replace');

// Fonts
gulp.task('fonts-mdi', function() {
    return gulp.src([
        'src/libs/mdi/fonts/*'])
        .pipe(gulp.dest('dist/fonts/mdi'));
});

gulp.task('fonts-devicon', function() {
    return gulp.src([
        'src/libs/devicon/fonts/*'])
        .pipe(gulp.dest('dist/fonts/devicon'));
});

gulp.task('copy-fonts', ['fonts-mdi', 'fonts-devicon']);


// CSS
gulp.task('devicon-sass-patch', function(){
    return gulp.src(['src/libs/devicon/devicon.css'])
        .pipe(replace(/url\(\'fonts\//g, 'url(\'../fonts/devicon/'))
        .pipe(gulp.dest('dist/libs/devicon/'))
});

gulp.task('sass', function () {
    return gulp.src(['src/scss/*.scss'])
        .pipe(compass({
            css: 'dist/css',
            sass: 'src/scss',
            environment: 'production'
        }))
});
gulp.task('minify-css', ['devicon-sass-patch', 'sass'], function() {
    return gulp.src(['dist/css/*.css'])
        .pipe(importCSS())
        .pipe(cleanCSS())
        .pipe(gulp.dest('dist/css/'));
});

// Image Assets
gulp.task('copy-images', function(){
    return gulp.src(['src/img/**/*'])
        .pipe(gulp.dest('dist/img'))
});


gulp.task('default', function() {
    // place code for your default task here
    gulp.start('minify-css', 'copy-fonts', 'copy-images');
});
