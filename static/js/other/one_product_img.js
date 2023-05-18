


let click_one_logo1 = document.querySelector(".one_logo1");
let click_one_logo2 = document.querySelector(".one_logo2");
let click_one_logo3 = document.querySelector(".one_logo3");
let click_one_logo4 = document.querySelector(".one_logo4");


let one_logo1 = document.querySelector("#one_logo1");
let one_logo2 = document.querySelector("#one_logo2");
let one_logo3 = document.querySelector("#one_logo3");
let one_logo4 = document.querySelector("#one_logo4");



click_one_logo1.addEventListener("click", appear_1);

if (click_one_logo2 != null) {
    click_one_logo2.addEventListener("click", appear_2);
}

if (click_one_logo3 != null) {
    click_one_logo3.addEventListener("click", appear_3);
}

if (click_one_logo4 != null) {
    click_one_logo4.addEventListener("click", appear_4);
}



function appear_1 () {
    one_logo1.style.display = "block";
    
    if (click_one_logo2 != null) {
    one_logo2.style.display = "none";
    } 
    if (click_one_logo3 != null) {
    one_logo3.style.display = "none";
    }
    if (click_one_logo4 != null) { 
    one_logo4.style.display = "none";
    }     
}

function appear_2 () {
    one_logo2.style.display = "block";

    one_logo1.style.display = "none";

    if (click_one_logo3 != null) {
    one_logo3.style.display = "none";
    }
    if (click_one_logo4 != null) {
    one_logo4.style.display = "none";
    } 
}

function appear_3 () {
    one_logo3.style.display = "block";

    one_logo1.style.display = "none";

    if (click_one_logo2 != null) {
    one_logo2.style.display = "none";
    }
    if (click_one_logo4 != null) {
    one_logo4.style.display = "none";
    }
}

function appear_4 () {
    one_logo4.style.display = "block";

    one_logo1.style.display = "none";

    if (click_one_logo2 != null) {
    one_logo2.style.display = "none";
    }
    if (click_one_logo3 != null) { 
    one_logo3.style.display = "none";
    } 
}
