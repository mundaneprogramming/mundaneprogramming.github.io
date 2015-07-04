
var util = require('util');
var system = require('system')
var optparse = require('optparse');
var switches = [
  ['-f', '--format FORMAT', 'image format. default is jpg'],
  ['-q', '--quality NUMBER', 'Quality from 0 to 100, default is 75'],
  ['-d', '--dim WIDTH_x_HEIGHT', 'Specify dimensions of viewport as [width]x[height]; default is 1200px wide, with height 2/3 of width'],
  ['-o', '--output FILENAME', 'Specify the output path of the filename' ],
  ['-h', '--help', 'Shows help'],
];

var parser = new optparse.OptionParser(switches);


var opts = {
  url: '',
  format: 'jpg',
  output_filename: '',
  quality: 75,
  dim:{
    width: 1200,
    height: 900
  }
}





parser.on('help', function(){
  console.dir(switches)
})

parser.on('output', function(e, val){
  opts['output_filename'] = val;
});

parser.on('format', function(e, val){
  opts['format'] = val;
})

parser.on('quality', function(e, val){
  opts['quality'] = parseInt(val);
})

parser.on('dim', function(e, val){
  var d = val.split('x');
  if(parseInt(d[0]) > 0){
    opts.dim.width = parseInt(d[0]);
  }
  if(parseInt(d[1]) > 0){
    opts.dim.height = parseInt(d[1]);
  }else{
    opts.dim.height = parseInt(opts.dim.width * (2/3));
  }
})

parser.on(1, function(uval){
  opts.url = uval;
})


// set output filename if not already set



parser.parse(system.args);

if(!opts.output_filename || opts.output_filename === ''){
  var fu = opts.url.split("//").slice(1).join('__');
  fu = fu.replace(/[^a-z0-9]/gi, '_').toLowerCase();
  opts.output_filename = fu + '.' + new Date().toISOString().replace(/:/g, '') +
    '.' + opts.format;
}




console.log('Parameters:');
console.log(util.inspect(opts, false, null));


var page = require('webpage').create();
page.open(opts.url, function() {
  page.viewportSize = opts.dim
  page.render(opts.output_filename);
  phantom.exit();
});







// var phantom = require("phantom")
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
