#!/usr/bin/node
let p = '';
p = parseInt(process.argv[2], 10);
if (Number.isNaN(p)) {
  console.log('Missing size');
} else {
  let i;
  let pr = '';
  for (i = 0; i < p; i++) {
    pr += 'X';
  }
  for (i = 0; i < p; i++) {
    console.log(pr);
  }
}
