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
        show_toast(data);
      }
    })
  })
})