var system = require('system')
var url = '';
optparse = require('optparse');
var switches = [
  ['-h', '--help', 'Shows help']
];

var parser = new optparse.OptionParser(switches);

parser.on('help', function(){
  console.log("Help there")
})

parser.on(1, function(value){
  url = value;
})



parser.parse(system.args);

console.log('Hello, world!');

console.log('URL is: ' + url)

phantom.exit();






// var phantom = require("phantom")
// var page = require('webpage').create();
// var assert = require('assert');


// var argv = require('yargs').argv;

// phantom.exit();

// // console.log(argv);

// var url = system.args[1]
// console.log(url)


// var argv = require('minimist')(phantom.args)


// var system = require('system');
// // var page = require('webpage').create();
// https://gist.github.com/DanHerbert/9520689
// var argv = require('minimist')(process.argv.slice(2));
// console.log("hey ")



// // set args
// var url = phantom.args[0]
// // set output filename
// if( casper.cli.has("output")) {
//   var fname = casper.cli.get("output")
// } else{
//   var fname = safeurltofilename(url) + '.' + new Date().toISOString().replace(/:/g, '') +
//     '.' + fileformat;
// }






// page.open(url, function() {
//   page.render('github.png');
//   phantom.exit();
// });


// usage
// casper thisscript.js urltosnapshot.com --output optional-filename.jpg
// doesn't work on https

// const DEF_FORMAT = "jpg";
// const DEF_QUALITY = 75;
// const DEF_WIDTH = 1200;
// const DEF_WAIT = 1000

// function safeurltofilename(txt){
//   var s = txt.split("//").slice(1).join('__');
//   return s.replace(/[^a-z0-9]/gi, '_').toLowerCase();
// }

// var casper = require('casper').create();


// var url = casper.cli.args[0]

// // set extension
// if( casper.cli.has("format")) {
//   var fileformat = casper.cli.get("format")
// } else{
//   var fileformat = DEF_FORMAT;
// }

// if( casper.cli.has("quality")) {
//   var filequality = parseInt(casper.cli.get("quality"));
// } else{
//   var filequality = DEF_QUALITY;
// }


// // set dimensions
// var viewportdim = {"top": 0, "left": 0};
// if( casper.cli.has("width")) {
//   viewportdim["width"] = parseInt(casper.cli.get("width"));
// }else{
//   viewportdim["width"] = 1200;
// }

// if( casper.cli.has("height")) {
//   viewportdim["height"] = parseInt(casper.cli.get("height"));
// }else{
//   viewportdim["height"] = viewportdim["width"] * 9.0 / 16.0;
// }

// // set output filename
// if( casper.cli.has("output")) {
//   var fname = casper.cli.get("output")
// } else{
//   var fname = safeurltofilename(url) + '.' + new Date().toISOString().replace(/:/g, '') +
//     '.' + fileformat;
// }


// // set waiting period
// if( casper.cli.has("wait")) {
//   var waitms = parseInt(casper.cli.get("wait"))
// } else{
//   var waitms = DEF_WAIT;
// }


// // run it
// casper.start(url, function(){
//   this.thenOpen(url).wait(waitms, function(){
//     this.viewport(viewportdim.width, viewportdim.height);
//     this.echo("Capturing " + url + ", title: " + this.getTitle());
//   });

//   this.then(function(){
//     this.echo("Saving to " + fname);
//     this.capture(fname, viewportdim, {format: fileformat, quality: filequality});
//   });
// });

// casper.run();
