#!/usr/bin/node
let p = '';
p = parseInt(process.argv[2], 10);
if (Number.isNaN(p)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + p);
}
