#!/usr/bin/node
/*
* Task 9
*/
var i = 0;
exports.logMe = function (item) {
  console.log(`${i}: ${item}`);
  i++;
};
