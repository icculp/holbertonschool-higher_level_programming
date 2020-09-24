#!/usr/bin/node
/*
* Task 9
*/
const $ = window.$;
$.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('div#hello').append(data.hello);
});
