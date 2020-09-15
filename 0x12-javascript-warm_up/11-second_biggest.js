#!/usr/bin/node
const f = parseInt(process.argv[2], 10);
if (Number.isNaN(f) || process.argv.length <= 3) {
  console.log(0);
} else {
  const j = process.argv.slice(2);
  const m = Math.max(...j);
  const i = j.indexOf(String(m));
  j[i] = -Infinity;
  console.log(Math.max(...j));
}
