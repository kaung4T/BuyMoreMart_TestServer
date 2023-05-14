


let accessories_left = document.querySelector(".accessories_left");
let accessories_right = document.querySelector(".accessories_right");
let accessories_left2 = document.querySelector(".accessories_left2");
let accessories_right2 = document.querySelector(".accessories_right2");
let accessories_products = document.querySelector(".accessories_products");


accessories_left.addEventListener("click", a_left);
accessories_right.addEventListener("click", a_right);


accessories_right2.addEventListener("click", a_left2);
accessories_right2.addEventListener("click", a_right2);

function a_left () {
    accessories_products.scrollBy(-350, 0);
}


function a_right () {
    accessories_products.scrollBy(350, 0);
}



function a_left2 () {
    accessories_products.scrollBy(-200, 0);
}


function a_right2 () {
    accessories_products.scrollBy(215, 0);
}
