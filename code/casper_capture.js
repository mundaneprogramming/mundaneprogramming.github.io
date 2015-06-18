var casper = require('casper').create();

casper.start('http://ogesdw.dol.gov/homePage.php', function(){
  this.echo(this.getTitle());
  this.capture("/tmp/ogesw.jpg");
});

casper.run();
