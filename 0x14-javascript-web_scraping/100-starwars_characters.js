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
    for (let i = 0; i < jj.characters.length; i++) {
      const newurl = jj.characters[i];
      req(newurl, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const j = JSON.parse(body);
          console.log(j.name);
        }
      });
    }
  }
});
