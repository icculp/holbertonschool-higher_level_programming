#!/usr/bin/node
/*
* Task 4
*/
const req = require('request');
const url = process.argv[2];
req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jj = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < jj.results.length; i++) {
      for (let j = 0; j < jj.results[i].characters.length; j++) {
        if (jj.results[i].characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
