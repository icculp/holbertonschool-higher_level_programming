#!/usr/bin/node
/*
* Task 7
*/
const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jj = JSON.parse(body);
    for (let i = 0; i < jj['characters'].length; i++) {
      console.log(jj.characters[i]);
    }
  }
});
