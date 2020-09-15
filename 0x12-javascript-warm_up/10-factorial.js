#!/usr/bin/node
const f = parseInt(process.argv[2], 10);
function fact (a) {
  if (a === 1) {
    return (1);
  } else {
    return a * fact(a - 1);
  }
}
if (Number.isNaN(f)) {
  console.log(1);
} else {
  console.log(fact(f));
}
