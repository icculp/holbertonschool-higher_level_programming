#!/usr/bin/node
/*
* Task 0
*/
const fs = require('fs');
const fn = process.argv[2];
fs.readFile(fn, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
