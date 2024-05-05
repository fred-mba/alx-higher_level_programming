/* Fetches and lists the title for all movies by using this URL: */
$.ajax({
  method: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function (response) {
    const movies = response.results;

    for (const movie of movies) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    }
  },
  error: function (xhr, status, error) {
    console.error(error);
  }
});
