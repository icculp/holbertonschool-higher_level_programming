#!/usr/bin/node
/*
* Task 7
*/
const $ = window.$;
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  console.log(data.results);
  for (const r of data.results) {
    $('ul#list_movies').append('<li>' + r.title + '</li>\n </br>');
  }
});
