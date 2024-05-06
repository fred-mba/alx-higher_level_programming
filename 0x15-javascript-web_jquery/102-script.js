/**
 * Fetches and prints how to say “Hello” depending on the language
 * The language code will be the value entered in the tag INPUT#language_code
 * The translation must be fetched when the user clicks on INPUT#btn_translate
 * The translation of “Hello” must be displayed in the HTML tag DIV#hello
 * Script must work when imported from the <head> tag
*/
$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    const langCode = $('#language_code').val();
    $.ajax({
      method: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      data: { lang: langCode },
      success: function (response) {
        $('#hello').text(response.hello);
      },
      error: function (xhr, status, error) {
        console.error(error);
      }
    });
  });
});
