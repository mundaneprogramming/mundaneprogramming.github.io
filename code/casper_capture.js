// usage
// casper thisscript.js urltosnapshot.com --output optional-filename.jpg
// doesn't work on https

const DEF_FORMAT = "jpg";
const DEF_QUALITY = 75;
const DEF_WIDTH = 1200;
const DEF_WAIT = 1000

function safeurltofilename(txt){
  var s = txt.split("//").slice(1).join('__');
  return s.replace(/[^a-z0-9]/gi, '_').toLowerCase();
}

var casper = require('casper').create();


var url = casper.cli.args[0]

// set extension
if( casper.cli.has("format")) {
  var fileformat = casper.cli.get("format")
} else{
  var fileformat = DEF_FORMAT;
}

if( casper.cli.has("quality")) {
  var filequality = parseInt(casper.cli.get("quality"));
} else{
  var filequality = DEF_QUALITY;
}


// set dimensions
var viewportdim = {"top": 0, "left": 0};
if( casper.cli.has("width")) {
  viewportdim["width"] = parseInt(casper.cli.get("width"));
}else{
  viewportdim["width"] = 1200;
}

if( casper.cli.has("height")) {
  viewportdim["height"] = parseInt(casper.cli.get("height"));
}else{
  viewportdim["height"] = viewportdim["width"] * 9.0 / 16.0;
}

// set output filename
if( casper.cli.has("output")) {
  var fname = casper.cli.get("output")
} else{
  var fname = safeurltofilename(url) + '.' + new Date().toISOString().replace(/:/g, '') +
    '.' + fileformat;
}


// set waiting period
if( casper.cli.has("wait")) {
  var waitms = parseInt(casper.cli.get("wait"))
} else{
  var waitms = DEF_WAIT;
}


// run it
casper.start(url, function(){
  this.thenOpen(url).wait(waitms, function(){
    this.viewport(viewportdim.width, viewportdim.height);
    this.echo("Capturing " + url + ", title: " + this.getTitle());
  });

  this.then(function(){
    this.echo("Saving to " + fname);
    this.capture(fname, viewportdim, {format: fileformat, quality: filequality});
  });
});

casper.run();
