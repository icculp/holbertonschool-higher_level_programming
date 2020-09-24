#!/usr/bin/node
/*
* Task 11
*/
const $ = window.$;

function doSomething () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  $('div#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  $('div#clear_list').click(function () {
    $('ul.my_list').empty();
  });
}

if (document.readyState === 'loading') { // Loading hasn't finished yet
  document.addEventListener('DOMContentLoaded', doSomething);
} else { // `DOMContentLoaded` has already fired
  doSomething();
}
