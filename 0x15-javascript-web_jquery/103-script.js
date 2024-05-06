/**
 * Fetches and prints how to say “Hello” depending on the language
 * The language code will be the value entered in the tag INPUT#language_code
 * The translation must be fetched when the user clicks on INPUT#btn_translate OR
 * presses ENTER when the focus is on INPUT#language_code
 * The translation of “Hello” must be displayed in the HTML tag DIV#hello
 * Script must work when imported from the <head> tag
*/
$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    translateHello();
  });

  $('#language_code').on('keydown', function (event) {
    if (event.key === 'ENTER') {
      translateHello();
    }
  });

  function translateHello () {
    const langCode = $('#language_code').val();
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      data: { lang: langCode },
      success: function (response) {
        $('#hello').text(response.hello);
      },
      error: function (xhr, status, error) {
        console.log(error);
      }
    });
  }
});
