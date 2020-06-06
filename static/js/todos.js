// alert("CONNECTED!!");

//strike todos by clicking
// $("ul").on("click", "li", function(){
// 	$(this).toggleClass("completed");	
// });


var li = document.querySelector("li");
li.addEventListener("click", function(){
	this.classList.toggle("completed");
});





