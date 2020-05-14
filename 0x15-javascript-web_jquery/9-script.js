$(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr'
  }).done(function (data) {
    $('#hello').text(data.hello);
  });
});
