



let default_setting = document.querySelector("#default_setting");
let main_default_page = document.querySelector(".main_default_page");
let second_default_page = document.querySelector(".second_default_page");
let default_closer = document.querySelector("#default_closer");

let default_body = document.body;


default_setting.addEventListener("click", setting_on);
second_default_page.addEventListener("click", setting_off);
default_closer.addEventListener("click", setting_off_with_cross);


function setting_on () {
    main_default_page.style.display = "block";
    second_default_page.style.display = "block";
    default_body.style.overflow = "hidden";
}


function setting_off () {
    main_default_page.style.display = "none";
    second_default_page.style.display = "none";
    default_body.style.overflow = "auto";
}



function setting_off_with_cross () {
    main_default_page.style.display = "none";
    second_default_page.style.display = "none";
    default_body.style.overflow = "auto";
}