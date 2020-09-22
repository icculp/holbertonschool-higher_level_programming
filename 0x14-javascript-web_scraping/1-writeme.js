#!/usr/bin/node
/*
* Task 1
*/
const fs = require('fs');
const fn = process.argv[2];
const str = process.argv[3];
fs.writeFile(fn, str, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
