
var x = window.matchMedia("(max-width: 482px)");

let fixed_mobile_second_header_content = document.querySelector(".mobile_second_header_content");
let fixed_mobile_third_header_content = document.querySelector(".mobile_third_header_content");

let fixed_ms2 = document.querySelector(".mobile_search_form_submit2");
fixed_ms2.addEventListener("click", clicker);


let second_header_content = document.querySelector(".mobile_second_header_content_fixed");
let mobile_third_header_content = document.querySelector(".mobile_third_header_content");

let fixed_second_mobile_searchheader_content2 = document.querySelector(".second_mobile_searchheader_content2");
let fixed_mobile_search_form = fixed_second_mobile_searchheader_content2.querySelector(".mobile_search_form");
let fixed_mobile_search_form_input = fixed_second_mobile_searchheader_content2.querySelector(".mobile_search_form_input");


let second_element_position = second_header_content.getBoundingClientRect().top
let third_element_position = mobile_third_header_content.getBoundingClientRect().top
let clicked = false;


function clicker () {
    clicked = true
    let current_scroll = window.scrollY;
    
    if (current_scroll > 190 && screen.width < 493) {
        fixed_second_mobile_searchheader_content2.style.position = "fixed";
        fixed_second_mobile_searchheader_content2.style.top = "70px";
    }
}


window.addEventListener("scroll", fun);




function fun () {

    let current_scroll = window.scrollY;
    

    if (current_scroll > 190 && screen.width < 493 && clicked) {
        
        second_header_content.style.animation = "header_effect 0.7s";
        second_header_content.style.position = "fixed";
        second_header_content.style.top = "0";
        second_header_content.style.width = "100%";
        second_header_content.style.background = "white";
        

        mobile_third_header_content.style.animation = "header_effect 0.7s";
        mobile_third_header_content.style.position = "fixed";

        // fixed_mobile_second_header_content.style.height = "155px";
        // fixed_mobile_third_header_content.style.top = "155px";
    }

    else if (current_scroll > 190 && screen.width < 493 && !clicked) {
        // second_header_content.style.transition = "top 0.1s ease";
        second_header_content.style.animation = "header_effect 0.7s";

        second_header_content.style.position = "fixed";
        second_header_content.style.top = "0";
        second_header_content.style.width = "100%";
        second_header_content.style.background = "white";
        fixed_mobile_second_header_content.style.padding = "20px 0 10px 0";



        // mobile_third_header_content.style.transition = "top 0.1s ease";
        mobile_third_header_content.style.animation = "header_effect 0.7s";

        mobile_third_header_content.style.position = "fixed";
        mobile_third_header_content.style.top = "90px";

    }
    else {
        second_header_content.style.position = "static";
        mobile_third_header_content.style.position = "static";

        fixed_mobile_second_header_content.style.padding = "30px 0 30px 0";
        
        fixed_second_mobile_searchheader_content2.style.position = "static";
        fixed_second_mobile_searchheader_content2.style.padding = "10px 0 0 0";
        fixed_mobile_second_header_content.style.height = "auto";
    }
    
}


