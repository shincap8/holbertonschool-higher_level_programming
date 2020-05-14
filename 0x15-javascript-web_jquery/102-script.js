$(function () {
  $('#btn_translate').click(function () {
    $.ajax({
      url: 'https://fourtonfish.com/hellosalut/?lang=' + $('#language_code').val()
    }).done(function (data) {
      $('#hello').text(data.hello);
    });
  });
});
