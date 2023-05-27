


let foods_left = document.querySelector(".foods_left");
let foods_right = document.querySelector(".foods_right");
let foods_left2 = document.querySelector(".foods_left2");
let foods_right2 = document.querySelector(".foods_right2");
let foods_products = document.querySelector(".foods_products");


foods_left.addEventListener("click", f_left);
foods_right.addEventListener("click", f_right);


foods_left2.addEventListener("click", f_left2);
foods_right2.addEventListener("click", f_right2);

function f_left () {
    foods_products.scrollBy(-350, 0);
}


function f_right () {
    foods_products.scrollBy(350, 0);
}



function f_left2 () {
    foods_products.scrollBy(-200, 0);
}


function f_right2 () {
    foods_products.scrollBy(215, 0);
}
