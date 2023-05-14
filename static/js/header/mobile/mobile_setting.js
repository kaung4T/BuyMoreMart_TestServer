



let mobile_setting = document.querySelector("#mobile_setting");
let main_mobile_page = document.querySelector(".main_mobile_page");
let second_mobile_page = document.querySelector(".second_mobile_page");
let mobile_closer = document.querySelector("#mobile_closer");

let body2 = document.body;

// let body2 = document.body;

// mobile_setting.addEventListener("click", fun);


// function fun () {
//     body2.classList.toggle("mobile_tab");
// };


mobile_setting.addEventListener("click", mobile_on);
second_mobile_page.addEventListener("click", mobile_off);
mobile_closer.addEventListener("click", mobile_off_with_cross);


function mobile_on () {
    main_mobile_page.style.display = "block";
    second_mobile_page.style.display = "block";
    body2.style.overflow = "hidden";
}


function mobile_off () {
    main_mobile_page.style.display = "none";
    second_mobile_page.style.display = "none";
    body2.style.overflow = "auto";
}



function mobile_off_with_cross () {
    main_mobile_page.style.display = "none";
    second_mobile_page.style.display = "none";
    body2.style.overflow = "auto";
}



