$(function () {
  $('#add_item, #remove_item, #clear_list').css('cursor', 'pointer');
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $('.my_list li:last-child').remove();
  });
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
