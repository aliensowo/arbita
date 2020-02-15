"use strict";

// === Packages ===
const { src, dest, parallel, series, watch  } = require('gulp');
const browserSync = require('browser-sync').create();
const debug = require('gulp-debug');
const rename = require('gulp-rename');
const uglify = require('gulp-uglify');
const sourcemaps = require('gulp-sourcemaps');
const concat = require('gulp-concat');
const minifyCSS = require('gulp-minify-css');
const prefix = require('gulp-autoprefixer');
const sass = require('gulp-sass');
const plumber = require('gulp-plumber');
const browserify = require('browserify');
const babelify = require('babelify');
const source = require( 'vinyl-source-stream' );
const buffer = require( 'vinyl-buffer' );

// === Src Files ===
const htmlWatch = 'dist/*.html';

const styleSRC = 'src/sass/style.scss';
const styleDist = 'dist/css/';
const styleWatch = 'src/sass/**/*.scss';

const jsSRC = 'script.js';
const jsFolder = 'src/js/';
const jsDIST = 'dist/js/';
const jsWatch = 'src/js/**/*.js';
const jsFiles = [jsSRC];

// === Browser Sync ===
function browseSync (done) {
    browserSync.init({
        server: {
            baseDir: "./dist/"
        }
    });
    
    done();
}

// === Html task ===
function html(done) {
    src(htmlWatch)
        .pipe(plumber())
        .pipe(browserSync.stream());
    
    done();
}

// === Css build task ===
function css(done) {
    src(styleSRC)
        .pipe(plumber())
        .pipe(sass())
        .pipe(concat("style.css"))
        .pipe(prefix('last 15 versions'))
        .pipe(minifyCSS(''))
        .pipe(dest(styleDist))
        .pipe(browserSync.stream());
    
    done();
}

// === Css dev task ===
function cssDev(done) {
    src(styleSRC)
        .pipe(plumber())
        .pipe(sourcemaps.init())
        .pipe(sass({
            errorLogToConsole: true,
            outputStyle: 'compressed'
        }))
        .on('error', console.error.bind(console))
        .pipe(concat("style.css"))
        .pipe(prefix({
            overrideBrowserslist: ['last 2 version'],
            cascade: false
        }))
        .pipe(minifyCSS(''))
        .pipe(sourcemaps.write('./'))
        .pipe(dest(styleDist))
        .pipe(browserSync.stream());
    
    done();
}

// === Js task ===
function js(done) {
    jsFiles.map(function ( entry ) {
        return browserify({
            entries: [ jsFolder + entry]
        })
            .transform( babelify, {presets: ['@babel/preset-env']} )
            .bundle()
            .pipe(source( entry ) )
            .pipe(rename ({ extname: '.min.js' }) )
            .pipe(buffer() )
            .pipe(sourcemaps.init({ loadMaps: true }))
            .pipe(uglify() )
            .pipe(sourcemaps.write())
            .pipe(dest(jsDIST) )
            .pipe(browserSync.stream());
    });
    
    done();
}

// === Tasks Watcher ===
function watcher(done) {
    watch(styleWatch, series(cssDev));
    watch(htmlWatch, series(html));
    watch(jsWatch, series(js));
    
    done();
}

exports.js = js;
exports.css = css;
exports.cssDev = cssDev;
exports.html = html;
exports.watcher = watcher;
exports.build = parallel(html, css, js);
exports.dev = parallel(browseSync, html, cssDev, js, watcher);