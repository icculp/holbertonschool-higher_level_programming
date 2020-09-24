#!/usr/bin/node
/*
* Task 3
*/
const $ = window.$;
$('div#red_header').click(function () {
  $('header').addClass('red').css('color', '#FF0000');
});
