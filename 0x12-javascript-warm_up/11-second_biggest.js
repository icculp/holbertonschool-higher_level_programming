#!/usr/bin/node
const f = parseInt(process.argv[2], 10);
if (Number.isNaN(f) || process.argv.length <= 3) {
  console.log(0);
} else {
  const j = process.argv.slice(2);
  console.log(j.sort()[j.length - 2]);
}
