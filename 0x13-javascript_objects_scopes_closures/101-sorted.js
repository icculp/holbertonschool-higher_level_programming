#!/usr/bin/node
/*
* Task 11
*/
const dict = require('./101-data.js').dict;
const mySet = new Set();
for (const value of Object.values(dict)) {
  mySet.add(value);
}
const newDict = {};
let i;
for (i = 0; i < mySet.size; i++) {
  const l = [];
  for (const [key, value] of Object.entries(dict)) {
    if (Array.from(mySet)[i] === value) {
      l.push(key);
    }
  }
  newDict[Array.from(mySet)[i]] = l;
}
console.log(newDict);
