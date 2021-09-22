$(document).ready(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(url, function (info) {
    $('DIV#hello').text(info.hello);
  });
});
