#!/usr/bin/node
/*
* Task 6
*/
const req = require('request');
const url = process.argv[2];
req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const j = JSON.parse(body);
    const dict = {};
    for (let i = 0; i < j.length; i++) {
      if (!(j[i].userId in dict) && j[i].completed === true) {
        dict[j[i].userId] = 0;
      }
      if (j[i].completed === true) {
        dict[j[i].userId] += 1;
      }
    }
    console.log(dict);
  }
});
