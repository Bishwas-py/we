

  function add_student(){
    $.ajax({
        url: '/student/add-student',
        type:'post',
        data:{
          'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val(),
          'student_name' : $("#student_name").val(),
          'student_short_name' : $("#student_short_name").val(),
          'student_address' : $("#student_address").val(),
          'student_father' : $("#student_father").val(),
          'student_mother' : $("#student_mother").val(),
          'student_fam_occupation' : $("#student_fam_occupation").val(),
          'admission_year' : $("#admission_year").val(),
          'admission_month' : $("#admission_month").val(),
          'admission_day' : $("#admission_day").val(),
          'dob_year' : $("#dob_year").val(),
          'dob_month' : $("#dob_month").val(),
          'dob_day' : $("#dob_day").val(),
          'student_phone_number': $("#student_phone_number").val(),
          'student_photo' : $("#student_photo").val(),
          'student_class' : $("#student_class").val()
        },
        success: function (data) {
            $('#toast-head-message').html(data['success_message']);
            $('#toast-head-message').attr("class", 'mr-auto -'+data['success_value']);
            $('#toast-success-or-faliure').attr("class", 'text-'+data['success_value']);
            $('#toast-success-or-faliure').html(data['success_remarks']);
            $('#toast-success-message').html(data['success_body']);
            $('.toast').toast('show')
        }
    })
}