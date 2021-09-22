const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url, function (info) {
  $('DIV#character').text(info.name);
});
