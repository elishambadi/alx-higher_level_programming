$(document).ready(function () {
  $('DIV#red_header').attr('class', 'red');
  $('#red_header').click(function () {
    // console.log('Red header clicked');
    $('DIV#red_header').toggleClass('green');
  });
});
