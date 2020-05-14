$(function () {
  $(document).on('keypress', function (e) {
    if (e.which === 13 && $('#language_code').is(':focus')) {
      language();
    }
  });
  $('#btn_translate').click(function () {
    language();
  });
});

function language () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=' + $('#language_code').val()
  }).done(function (data) {
    $('#hello').text(data.hello);
  });
}
