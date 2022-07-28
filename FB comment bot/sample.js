var count = 100; 
var message = "Hi"; 
var loop = setInterval(function(){ 
    var input = document.getElementsByName("comment_text")[0]; 
    var submit = document.querySelector('button[type="submit"]'); 
    submit.disabled = false; 
    input.value = message; 
    submit.click(); 
    count -= 1; 
    if(count == 0) 
    { 
        clearInterval(loop); 
    } 
}, 10000);