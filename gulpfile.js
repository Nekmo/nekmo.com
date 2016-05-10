process.chdir('nekmocom/static/nekmocom');
var gulp = require('gulp'),
    compass = require('gulp-compass');
    cleanCSS = require('gulp-clean-css');


// CSS
gulp.task('sass', function () {
    return gulp.src(['src/scss/*.scss'])
        .pipe(compass({
            css: 'dist/css',
            sass: 'src/scss',
            environment: 'production'
        }))
});
gulp.task('minify-css', ['sass'], function() {
    return gulp.src(['dist/css/*.css'])
        .pipe(cleanCSS())
        .pipe(gulp.dest('dist/css/'));
});


gulp.task('default', function() {
    // place code for your default task here
    gulp.start('minify-css');
});
