const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (info) {
  $.each(info.results, (i, film) => {
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  });
});
