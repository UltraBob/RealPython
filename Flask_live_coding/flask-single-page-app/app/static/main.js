$(document).ready(function() {
  console.log("ready!");

  $("form").on("submit", function() {
    console.log("the form has been submitted - yay!");

    var valueOne = $('input[name="location"]').val();
    var valueTwo = $('input[name="language"]').val();
    console.log(valueOne, valueTwo);

    $.ajax({
      type:  "POST",
      url:   "/",
      data: {first: valueOne, second: valueTwo},
      success: function(results) {
        console.log(results.items[0]);
        $("#results").html('<a href="'+results.items[0].html_url+'"><img src="'+results.items[0].avatar_url+'" /><br>'+results.items[0].login+'</a>');
        $("input").val("");
      },
      error: function(error) {
        console.log(error);
      }
    });
  });

});
