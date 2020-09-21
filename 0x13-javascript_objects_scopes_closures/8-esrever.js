#!/usr/bin/node
/*
* Task 8
*/
exports.esrever = function (list) {
  const rev = [];
  let i;
  let l = list.length - 1;
  for (i = 0; l >= 0; l--, i++) {
    rev[i] = list[l];
  }
  return rev;
};
