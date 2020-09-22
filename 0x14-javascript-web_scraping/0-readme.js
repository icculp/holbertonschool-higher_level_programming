#!/usr/bin/node
/*
* Task 0
*/
const fs = require('fs');
const fn = './' + process.argv[2];
fs.readFile(fn, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    process.stdout.write(data);
  }
});
