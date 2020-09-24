#!/usr/bin/node
/*
* Task 7
*/
const $ = window.$;
$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('div#character').append(data.name);
});
