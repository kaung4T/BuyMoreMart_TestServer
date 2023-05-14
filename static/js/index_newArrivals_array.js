


let newArrivals_left = document.querySelector(".newArrivals_left");
let newArrivals_right = document.querySelector(".newArrivals_right");
let newArrivals_left2 = document.querySelector(".newArrivals_left2");
let newArrivals_right2 = document.querySelector(".newArrivals_right2");
let newArrivals_products = document.querySelector(".newArrivals_products");


newArrivals_left.addEventListener("click", nw_left);
newArrivals_right.addEventListener("click", nw_right);


newArrivals_left2.addEventListener("click", nw_left2);
newArrivals_right2.addEventListener("click", nw_right2);

function nw_left () {
    newArrivals_products.scrollBy(-350, 0);
}


function nw_right () {
    newArrivals_products.scrollBy(350, 0);
}



function nw_left2 () {
    newArrivals_products.scrollBy(-200, 0);
}


function nw_right2 () {
    newArrivals_products.scrollBy(215, 0);
}
