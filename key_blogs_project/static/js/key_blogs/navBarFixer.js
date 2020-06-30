window.onscroll = function() {classChange()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function classChange() {
    var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrolled = (winScroll / height) * 100;
    document.getElementById("myBar").style.width = scrolled + "%";
    if(window.pageYOffset >= sticky){
        navbar.classList.add("fix");
    }
    else{
        navbar.classList.remove("fix");
    }
}