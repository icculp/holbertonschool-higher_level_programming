#!/usr/bin/node
/*
* Task 8
*/
const $ = window.$;
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const r of data.results) {
    $('ul#list_movies').append('<li>' + r.title + '</li>\n </br>');
  }
});
