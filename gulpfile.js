process.chdir('nekmocom/static/nekmocom');
var gulp = require('gulp'),
    compass = require('gulp-compass');
    cleanCSS = require('gulp-clean-css');
    importCSS = require('gulp-import-css');


// CSS
gulp.task('devicon-sass-patch', function(){
    return gulp.src(['src/libs/devicon/devicon.css'])
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
gulp.task('minify-css', ['sass', 'devicon-sass-patch'], function() {
    return gulp.src(['dist/css/*.css'])
        .pipe(importCSS())
        .pipe(cleanCSS())
        .pipe(gulp.dest('dist/css/'));
});


gulp.task('default', function() {
    // place code for your default task here
    gulp.start('minify-css');
});
