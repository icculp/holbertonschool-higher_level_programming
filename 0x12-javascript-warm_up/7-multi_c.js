#!/usr/bin/node
let p = '';
p = parseInt(process.argv[2], 10);
if (Number.isNaN(p)) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 0; i < p; i++) {
    console.log('C is fun');
  }
}
