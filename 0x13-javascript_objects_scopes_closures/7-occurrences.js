#!/usr/bin/node
/*
* Task 7
*/
exports.nbOccurences = function (list, searchElement) {
  let i;
  let c = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      c += 1;
    }
  }
  return c;
};
