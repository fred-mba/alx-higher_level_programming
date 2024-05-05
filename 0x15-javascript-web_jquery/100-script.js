/**
 * Script that updates the text color of the <header> element to red (#FF0000)
 * Must use document.querySelector to select the HTML tag
 * Script must be imported from the <head> tag, not at the end of the HTML
*/
document.addEventListener('DOMContentLoaded', function () {
  const heaDer = document.querySelector('header');
  heaDer.style.color = '#ff0000';
});
