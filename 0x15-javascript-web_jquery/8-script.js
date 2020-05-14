$(function () {
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json'
  }).done(function (data) {
    $.each(data.results, function (i, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
