#!/usr/bin/node
/*
* Task 6
*/
const $ = window.$;
$('div#update_header').click(function () {
  $('header').replaceWith('<header>New Header!!!</header>');
});
