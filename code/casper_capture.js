// sample URL http://ogesdw.dol.gov/homePage.php


function safeurltofilename(txt){
  var s = txt.split("//").slice(1).join('__');
  return s.replace(/[^a-z0-9]/gi, '_').toLowerCase();
}


var casper = require('casper').create();
var url = casper.cli.args[0]
if( casper.cli.has("output")) {
  var fname = casper.cli.get("output")
} else{
  var fname = safeurltofilename(url) + '.' + new Date().toISOString() + '.jpg'
}

casper.start(url, function(){
  this.echo("Capturing " + url + ", title: " + this.getTitle());
  this.capture(fname)
  this.echo("Saving to " + fname);
})
casper.run();
