function edit(editwhat) {
    var val = document.getElementById('bt_' + editwhat).innerHTML;

    switch (val) {
        case 'EDIT':
            console.log('edit_' + editwhat)
            document.getElementById('edit_' + editwhat).innerHTML = "<input class='form-control' type='text' name='" + editwhat + "' id='" + editwhat + "' required/><button class='btn btn-link' id='bt_" + editwhat + "' onclick=edit('" + editwhat + "')>CLOSE</button><button id='buttonId" + editwhat + "' style='color:red;cursor:pointer;' class='btn btn-link'>SUBMIT</button>";
            if (editwhat == 'principal') {
                document.getElementsByName('principal')[0].setAttribute('mexlength', '150');
                document.getElementsByName('principal')[0].setAttribute('minlength', '5');
                // document.getElementById('buttonId1')[0].setAttribute('class', 'btn btn-primary principalName');
            }
            if (editwhat == 'address') {
                document.getElementsByName('address')[0].setAttribute('mexlength', '100');
                document.getElementsByName('address')[0].setAttribute('minlength', '7');
            }
            if (editwhat == 'password') {
                document.getElementsByName('password')[0].setAttribute('type', 'password');
                document.getElementsByName('password')[0].setAttribute('mexlength', '95');
                document.getElementsByName('password')[0].setAttribute('minlength', '8');
            }
            break;
        case 'CLOSE':

            document.getElementById('edit_' + editwhat).innerHTML = "<button class='btn btn-link' id='bt_" + editwhat + "' onclick = edit('" + editwhat + "')>EDIT</button>";
            break;
    }
}