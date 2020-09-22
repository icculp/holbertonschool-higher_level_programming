#!/usr/bin/node
/*
* Task 2
*/
const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const j = response.toJSON();
    const jj = JSON.parse(j.body);
    console.log(jj.title);
  }
});
