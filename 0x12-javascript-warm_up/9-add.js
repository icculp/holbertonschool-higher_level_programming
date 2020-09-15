#!/usr/bin/node
const f = parseInt(process.argv[2], 10);
const s = parseInt(process.argv[3], 10);
function add (a, b) {
  return a + b;
}
if (Number.isNaN(f) || Number.isNaN(s)) {
  console.log('NaN');
} else {
  console.log(add(f, s));
}
