// alert("CONNECTED!!");

// strike todos by clicking
$("ul").on("click", "li", function(){
	$(this).toggleClass("completed");	
});


// var li = document.querySelectorAll("li");
// li.addEventListener("click", function(){
// 	this.classList.toggle("completed");
// });

//click on X to delete
$("ul").on("click", "button", function(event){
	$(this).parent().fadeOut(500, function(){
		$(this).remove();
	});
	event.stopPropagation(); //stop event bubbling
})



