#!/usr/bin/node
/*
* Task 9
*/
const $ = window.$;

function doSomething () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('div#hello').append(data.hello);
  });
}

if (document.readyState === 'loading') { // Loading hasn't finished yet
  document.addEventListener('DOMContentLoaded', doSomething);
} else { // `DOMContentLoaded` has already fired
  doSomething();
}
