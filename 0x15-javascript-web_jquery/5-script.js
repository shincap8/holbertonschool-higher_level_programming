$(function () {
  $('#add_item').css('cursor', 'pointer');
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
});
