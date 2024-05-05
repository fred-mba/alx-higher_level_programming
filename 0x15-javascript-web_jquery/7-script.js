/**
 * Fetches the character name from URL
 * The name must be displayed in the HTML tag DIV#character
 */
$.ajax({
  method: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  success: function (response) {
    $('DIV#character').text(response.name);
  },
  error: function (xml, status, error) {
    console.error(error);
  }
});
