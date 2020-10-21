  function create_class() { //Return the maximum Days in Nepali Date System (Bikram Sambat)
      var Class = document.getElementById('classInput').value;
      if (Class) {
          $.ajax({
              url: '/school/add-class',
              type: 'post',
              data: {
                  'class': Class,
                  'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
              },
              success: function (data) {
                  created = document.getElementById("class-created")
                  if (data == 2) {
                      created.innerHTML = "<span class='bg-danger' style='color:white;font-weight:bold;padding:2px;'>" + Class + "</span>" + ' is already created.';
                  } else if (data == 0) {
                      created.innerHTML = "<span class='bg-danger' style='color:white;font-weight:bold;padding:2px;'>" + Class + "</span>" + ' is not a valid class name. <b>TRY</b>: Class 1, Class 2, Class 3, Class 4, Class 5, Class 6, Class 7, Class 8, Class 9, Class 10, Class 11 and Class 12. <b>OR</b> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 and 12. <b>OR</b> Montessori, Nursery, L.K.G, U.K.G, Kindergarten, Kinder Garten & K.G';
                  } else {
                      var option = new Option(data, data);
                      /// jquerify the DOM object 'o' so we can use the html method
                      $(option).html(data);
                      $("#classoptions").append(option);
                      $("#classoptions").val(data);
                      created.innerHTML = "<span class='bg-success' style='color:white;font-weight:bold;padding:2px;'>" + data + "</span>" + ' created.';

                  }
              }

          })
      }


  }

  function automatic_class() {
      $.ajax({
          url: '/school/auto-class-create',
          type: 'post',
          data: {
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
          success: function (data) {
              if (data == 1) {
                  class_list = ['Nursery', 'L.K.G', 'U.K.G', 'Kindergarten', 'Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6', 'Class 7', 'Class 8', 'Class 9', 'Class 10']
                  for (i = 0; i < class_list.length; i++) {

                      var option = new Option(class_list[i], class_list[i]);
                      /// jquerify the DOM object 'o' so we can use the html method
                      $(option).html(class_list[i]);
                      $("#classoptions").append(option);

                  }
                  $('#auto-class-created').innerHTML = "<span class='bg-success' style='color:white;font-weight:bold;padding:2px;'>" + class_list + "</span>" + ' created.';

              }
              else{
                $('#auto-class-created').innerHTML = "<span class='bg-success' style='color:white;font-weight:bold;padding:2px;'>Failed to create class automatically.";
              }
          }
      })
  }