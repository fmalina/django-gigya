var gulp = require('gulp');
var plumber = require('gulp-plumber');
var notify = require('gulp-notify');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var uglify = require('gulp-uglify');
var sass = require('gulp-sass');
var sourcemaps = require('gulp-sourcemaps');
var autoprefixer = require('autoprefixer');
var postcss = require('gulp-postcss');
var gulpif = require('gulp-if');
var csso = require('gulp-csso');
var browsersync = require('browser-sync').create();

var config = require('./conf/gulp_config.json');

function plumberSCSSHandler(error) {
    notify.onError({
        title: 'Gulp',
        message: '\n<%= error.formatted %>'
    })(error);
    this.emit('end');
    this.destroy();
}

/**********************************************************************************************************************
 *** CLIENT **********************************************************************************************************/

function buildClientScss(isWatching) {
    // postcss is disable while watching because it significally slowers scss build
    var optionalPostcss = gulpif(!isWatching,
        postcss([
            autoprefixer()
        ])
    );

    return gulp.src(config.src.scss.entry.client)
        .pipe(plumber(plumberSCSSHandler))
        .pipe(sourcemaps.init())
        .pipe(sass({
            includePaths: config.src.scss.paths
        }))
        .pipe(optionalPostcss)
        .pipe(gulpif(!isWatching, csso()))
        .pipe(sourcemaps.write('./maps'))
        .pipe(gulp.dest(config.dest.client+'css'));
}

gulp.task('client:scss', function() {
    return buildClientScss(false)
});

gulp.task('client:scss:watch', function() {
    return buildClientScss(true)
        .pipe(browsersync.stream({match: "**/*.css"}))
});

gulp.task('client:fonts', function() {
    return gulp.src(config.src.fonts)
        .pipe(gulp.dest(config.dest.client+'fonts'))
});

gulp.task('client:browsersync', function() {
    browsersync.init(config.browsersync);
});

gulp.task('client:watch', function () {
    gulp.watch(config.src.scss.client, ['client:scss:watch']);
    gulp.watch(config.src.js, browsersync.reload);
});

gulp.task('client:build', [
    'client:scss',
    'client:fonts'
]);

gulp.task('client:serve', [
    'client:build',
    'client:watch',
    'client:browsersync'
]);

gulp.task('default', [
    'client:build'
]);
