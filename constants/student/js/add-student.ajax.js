$(document).ready(function () {
  $("#add-student-form").on('submit', function (event) {
    event.preventDefault();
    form_data = new FormData(this);
    console.log(form_data)
    $.ajax({
      url: '/student/add-student',
      type: 'post',
      data: form_data,
      processData: false,
      contentType: false,
      success: function (data) {
        $('#toast-head-message').html(data['success_message']);
        $('#toast-head-message').attr("class", 'mr-auto -' + data['success_value']);
        $('#toast-success-or-faliure').attr("class", 'text-' + data['success_value']);
        $('#toast-success-or-faliure').html(data['success_remarks']);
        $('#toast-success-message').html(data['success_body']);
        $('.toast').toast('show')
      }
    })
  })
})