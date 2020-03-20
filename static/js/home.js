
// Filter
const openFiltir = () => {
        document.getElementById('filtirnav').style.transform = "translateX(0)";
        document.getElementById('filtir-nav').style.display = "none";
};

const closeFiltir = () => {
    document.getElementById('filtirnav').style.transform = "translateX(-230px)";
    document.getElementById('filtir-nav').style.display = "block";
};

// Scroll Navbar
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("navbar").style.top = "0";
    } else {
        document.getElementById("navbar").style.top = "-100px";
    }
    prevScrollpos = currentScrollPos;
};

// Registration
const registrUserEnter = () => {
    document.getElementById('registr').style.display = "block";
};
const registrUserLeave = () => {
    document.getElementById('registr').style.display = "none";
};

// Menu-Nav
let openNav = true;
const menuCloseOpen = () => {
        if (openNav){
            document.getElementById("menu-nav").style.left = "0";
            openNav = false;
        } else {
            document.getElementById("menu-nav").style.left = "-230px";
            openNav = true;
        }
};

let collapseNav = true;
const collapse = () =>{
    if(collapseNav){
        document.getElementById('menuAllCategories').style.height = '280px';
        document.getElementById("iconUpDown").classList.remove("icon-arrow-down");
        document.getElementById("iconUpDown").classList.add("icon-arrow-up");
        document.getElementById("iconUpDown").style.backgroundColor = "white";
        collapseNav = false;
    } else {
        document.getElementById('menuAllCategories').style.height = '0';
        document.getElementById("iconUpDown").classList.remove("icon-arrow-up");
        document.getElementById("iconUpDown").classList.add("icon-arrow-down");
        document.getElementById("iconUpDown").style.backgroundColor = "white";
        collapseNav = true;
    }
};


// Category
let scanOffOn = true;
const allCategory = () => {
    if (scanOffOn){
        document.getElementById('allCategory').style.height = "350px";
        scanOffOn = false;
    } else {
        document.getElementById('allCategory').style.height = "0";
        scanOffOn = true;
    }
};

// Search
const openSearch = () => {
    document.getElementById('open-search').style.top = '0';
};
const closeSearch = () => {
    document.getElementById('open-search').style.top = '-85px';
};

//Basket
const modalCart = () => {
        document.getElementById('modal-cart').style.display = "block";
};
const modalCloseCart = () => {
    document.getElementById('modal-cart').style.display = "none";
};

// About Us
let modal = document.getElementById('about-us');
let btn = document.getElementById("myBtn");
let span = document.getElementById('close');

btn.onclick = function() {
    modal.style.display = "block";
};
span.onclick = function() {
    modal.style.display = "none";
};
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
};

// Garranty
let modal1 = document.getElementById('garranty');
let btn1 = document.getElementById("myBtn1");
let span1 = document.getElementById('close-g');
btn1.onclick = function() {
    modal1.style.display = "block";
};
span1.onclick = function() {
    modal1.style.display = "none";
};
window.onclick = function(event) {
    if (event.target === modal1) {
        modal1.style.display = "none";
    }
};