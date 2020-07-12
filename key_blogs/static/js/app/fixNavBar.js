window.onscroll = function() {classChange()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function classChange() {
    if(window.pageYOffset >= sticky){
        navbar.classList.add("fix");
    }
    else{
        navbar.classList.remove("fix");
    }
}