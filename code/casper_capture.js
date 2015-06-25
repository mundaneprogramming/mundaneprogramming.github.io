var casper = require('casper').create();
// proof of concept
casper.start('http://ogesdw.dol.gov/homePage.php', function(){
  this.echo(this.getTitle());
  this.capture("/tmp/ogesw.jpg");
});

casper.run();
