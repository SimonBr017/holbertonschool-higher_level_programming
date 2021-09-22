$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?lang=';
  $('INPUT#btn_translate').click(function () {
    $.get(url + $('INPUT#language_code').val(), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
  $('INPUT#language_code').on('keypress', (event) => {
    if (event.key === 'Enter') {
      $.get(url + $('INPUT#language_code').val(), function (data) {
        $('DIV#hello').html(data.hello);
      });
    }
  });
});
