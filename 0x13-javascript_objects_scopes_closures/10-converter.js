#!/usr/bin/node
/*
* Task 9
*/
exports.converter = function (base) {
  return function (c) {
    return c.toString(base);
  };
};
