/**
 * Fetches from the url and displays the value of hello from that fetch in the
 * HTML tag DIV#hello
 * The translation of “hello” must be displayed in the HTML tag DIV#hello
 * The script must work when it is imported from the <head> tag
*/
$(document).ready(function () {
  $.ajax({
    method: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (response) {
      $('DIV#hello').text(response.hello);
    },
    error: function (xhr, status, error) {
      console.error(error);
    }
  });
});
