#!/usr/bin/node
/*
* Task 2
*/
const req = require('request');
const url = process.argv[2];
req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
