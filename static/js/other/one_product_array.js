


let one_product_left = document.querySelector(".one_product_left");
let one_product_right = document.querySelector(".one_product_right");
let one_product_left2 = document.querySelector(".one_product_left2");
let one_product_right2 = document.querySelector(".one_product_right2");
let one_products = document.querySelector(".one_products");


one_product_left.addEventListener("click", one_left);
one_product_right.addEventListener("click", one_right);


one_product_left2.addEventListener("click", one_left2);
one_product_right2.addEventListener("click", one_right2);

function one_left () {
    one_products.scrollBy(-350, 0);
}


function one_right () {
    one_products.scrollBy(350, 0);
}



function one_left2 () {
    one_products.scrollBy(-200, 0);
}


function one_right2 () {
    one_products.scrollBy(215, 0);
}
