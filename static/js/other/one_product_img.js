


let click_one_logo1 = document.querySelector(".one_logo1");
let click_one_logo2 = document.querySelector(".one_logo2");
let click_one_logo3 = document.querySelector(".one_logo3");
let click_one_logo4 = document.querySelector(".one_logo4");


let one_logo1 = document.querySelector("#one_logo1");
let one_logo2 = document.querySelector("#one_logo2");
let one_logo3 = document.querySelector("#one_logo3");
let one_logo4 = document.querySelector("#one_logo4");
alert(click_one_logo2);


click_one_logo1.addEventListener("click", appear_1);
click_one_logo2.addEventListener("click", appear_2);
click_one_logo3.addEventListener("click", appear_3);
click_one_logo4.addEventListener("click", appear_4);



function appear_1 () {
    one_logo1.style.display = "block";
    
    one_logo2.style.display = "none"; 
    one_logo3.style.display = "none"; 
    one_logo4.style.display = "none";     
}

function appear_2 () {
    one_logo2.style.display = "block";

    one_logo1.style.display = "none"; 
    one_logo3.style.display = "none"; 
    one_logo4.style.display = "none"; 
}

function appear_3 () {
    one_logo3.style.display = "block";

    one_logo1.style.display = "none"; 
    one_logo2.style.display = "none"; 
    one_logo4.style.display = "none"; 
}

function appear_4 () {
    one_logo4.style.display = "block";

    one_logo1.style.display = "none"; 
    one_logo2.style.display = "none"; 
    one_logo3.style.display = "none"; 
}
