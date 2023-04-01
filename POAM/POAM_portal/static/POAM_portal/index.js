document.addEventListener("DOMContentLoaded",function(){
    // Show active pages
    links = document.querySelectorAll(".nav-options li a");
    links.forEach(element => {
        if(element.href === window.location.href){
            element.setAttribute("id","activated");
        }
    })
})
