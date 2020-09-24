#!/usr/bin/node
/*
* Task 10
*/

function doSomething () {
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
}

if (document.readyState === 'loading') { // Loading hasn't finished yet
  document.addEventListener('DOMContentLoaded', doSomething);
} else { // `DOMContentLoaded` has already fired
  doSomething();
}
