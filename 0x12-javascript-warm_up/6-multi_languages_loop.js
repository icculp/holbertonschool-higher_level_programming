#!/usr/bin/node
const myVar = 'C is fun\nPython is cool\nJavascript is amazing\n';
let i;

for (i = 0; i < myVar.length; i++) {
  process.stdout.write(myVar[i]);
}
