


let beauty_left = document.querySelector(".beauty_left");
let beauty_right = document.querySelector(".beauty_right");
let beauty_left2 = document.querySelector(".beauty_left2");
let beauty_right2 = document.querySelector(".beauty_right2");
let beauty_products = document.querySelector(".beauty_products");


beauty_left.addEventListener("click", b_left);
beauty_right.addEventListener("click", b_right);


beauty_left2.addEventListener("click", b_left2);
beauty_right2.addEventListener("click", b_right2);

function b_left () {
    beauty_products.scrollBy(-350, 0);
}


function b_right () {
    beauty_products.scrollBy(350, 0);
}



function b_left2 () {
    beauty_products.scrollBy(-200, 0);
}


function b_right2 () {
    beauty_products.scrollBy(215, 0);
}
