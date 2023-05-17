
var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};


/*
//TESTING doesnt work...//
 $('.form2').hide();

 $('.myprofile').click(function(e) {
   e.preventDefault();
   $(this).addClass('active');
   $('.preferences').removeClass('active');
   $('.form1').show();
   $('.form2').hide();
 //  $('#edit-email').focus(); //Should appear after $('.login__form').show(); because if it's before that, the register form doesn't exist in the DOM
 });

 $('.preferences').click(function(e) {
   e.preventDefault();
   $(this).addClass('active');
   $('.myprofile').removeClass('active');
   $('.form2').show();
   $('.form1').hide();
//   $('#edit-firstname').focus(); //Should appear after $('.register__form').show(); because if it's before that, the register form doesn't exist in the DOM
 });
*/
