#!/usr/bin/node
/*
* Task 5
*/
const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const fn = process.argv[3];
req(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fn, body, 'utf-8', (err, body) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
/*
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
}); */
