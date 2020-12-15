function show_toast(data) {
    $('#toast-head-message').html(data['success_message']);
    $('#toast-head-message').attr("class", 'mr-auto -' + data['success_value']);
    $('#toast-success-or-faliure').attr("class", 'text-' + data['success_value']);
    $('#toast-success-or-faliure').html(data['success_remarks']);
    $('#toast-success-message').html(data['success_body']);
    $('.toast').toast('show')
}