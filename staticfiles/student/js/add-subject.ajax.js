$(document).ready(function () {
    $("#add-subject-form").on('submit', function (event) {
      event.preventDefault();
      form_data = new FormData(this);
      console.log(form_data)
      $.ajax({
        url: '/school/create-subjects',
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