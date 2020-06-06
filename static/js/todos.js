// alert("CONNECTED!!");

//strike todos by clicking
// $("ul").on("click", "li", function(){
// 	$(this).toggleClass("completed");	
// });


var ul = document.querySelector("ul");
ul.addEventListener("click", function(){
	ul.classList.toggle("completed");
});



