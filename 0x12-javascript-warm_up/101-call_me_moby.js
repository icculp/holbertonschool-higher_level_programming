#!/usr/bin/node
exports.callMeMoby = function (c, theFunction) {
  let i;
  for (i = 0; i < c; i++) {
    theFunction();
  }
};
