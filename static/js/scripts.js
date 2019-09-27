// Global variable
var img_name = "";

var upload = function() {
    $('#file').click();  //returns a jQuery Object
};

var displayImage = function() {
    var preview = document.querySelector('img');
    var file    = document.querySelector('input[type=file]').files[0];
    var reader = new FileReader();
    
    img_name = this.value.split("\\")[2];    
      
    reader.addEventListener("load", function () {
        $("#img-container").css("background-color", "white");
        preview.src = reader.result;
    }, false);

    if (file) {
        reader.readAsDataURL(file);
    }
};

$(document).ready(function() {
  $(document).on("click", "#upload-button", upload);
  $("#file").change(displayImage);
  $(document).keypress(function(e) {if(e.which === 13) {login();}});
  
  $(document).on("click", "#predict-button", function() {
    $.post({
      type: "POST",
      url: "/api/v1/" + img_name,
      success(response) {
       $("#prediction").text("Prediction: " + response.object_detected);
       $("#confidence").text("Confidence: " + response.confidence);
      }
    });
  });
});