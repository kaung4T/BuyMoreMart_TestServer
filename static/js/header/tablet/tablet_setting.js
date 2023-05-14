



let tablet_setting = document.querySelector("#tablet_setting");
let main_tablet_page = document.querySelector(".main_tablet_page");
let second_tablet_page = document.querySelector(".second_tablet_page");
let tablet_closer = document.querySelector("#tablet_closer");

let body = document.body;


// let body = document.body;
// let clicked = false;

// tablet_setting.addEventListener("click", fun);


// function fun () {
//     body.classList.toggle("tablet_tab");
// };


tablet_setting.addEventListener("click", tablet_on);
second_tablet_page.addEventListener("click", tablet_off);
tablet_closer.addEventListener("click", tablet_off_with_cross);


function tablet_on () {
    main_tablet_page.style.display = "block";
    second_tablet_page.style.display = "block";
    body.style.overflow = "hidden";
}


function tablet_off () {
    main_tablet_page.style.display = "none";
    second_tablet_page.style.display = "none";
    body.style.overflow = "auto";
}



function tablet_off_with_cross () {
    main_tablet_page.style.display = "none";
    second_tablet_page.style.display = "none";
    body.style.overflow = "auto";
}