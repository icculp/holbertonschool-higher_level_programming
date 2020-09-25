#!/usr/bin/node
/*
* Task 11
*/
const $ = window.$;

function doSomething () {
  $('input#btn_translate').click(function () {
    const inp = $('input#language_code').val();
    const ur = 'https://fourtonfish.com/hellosalut/?lang=' + inp;
    $.getJSON(ur, function (data) {
      $('div#hello').empty();
      $('div#hello').append(data.hello);
    });
  });
}

if (document.readyState === 'loading') { // Loading hasn't finished yet
  document.addEventListener('DOMContentLoaded', doSomething);
} else { // `DOMContentLoaded` has already fired
  doSomething();
}
