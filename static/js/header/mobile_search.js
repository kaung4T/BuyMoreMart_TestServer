



let ms = document.querySelector(".mobile_search_form_submit");
let ms2 = document.querySelector(".mobile_search_form_submit2");

let se_mobile_second_header_content = document.querySelector(".mobile_second_header_content");
let se_mobile_third_header_content = document.querySelector(".mobile_third_header_content");


// let search_line_arrow = document.querySelector(".search_line_arrow");


let second_mobile_searchheader_content = document.querySelector(".second_mobile_searchheader_content");
let mobile_search_form = second_mobile_searchheader_content.querySelector(".mobile_search_form");
let mobile_search_form_input = second_mobile_searchheader_content.querySelector(".mobile_search_form_input");
let mobile_search_form_cancel = second_mobile_searchheader_content.querySelector(".mobile_search_form_cancel");



let second_mobile_searchheader_content2 = document.querySelector(".second_mobile_searchheader_content2");
let mobile_search_form2 = second_mobile_searchheader_content2.querySelector(".mobile_search_form");
let mobile_search_form_input2 = second_mobile_searchheader_content2.querySelector(".mobile_search_form_input");
let mobile_search_form_cancel2 = second_mobile_searchheader_content2.querySelector(".mobile_search_form_cancel2");



let search_body = document.body; 


ms.addEventListener("click", fun);
ms2.addEventListener("click", fun2);

mobile_search_form_cancel.addEventListener("click", cancel1);
mobile_search_form_cancel2.addEventListener("click", cancel2);



function fun () {
    second_mobile_searchheader_content.style.display = "block";
    mobile_search_form.style.display = "flex";
    mobile_search_form_input.style.display = "block";
    mobile_search_form_cancel.style.display = "block";
};

function fun2 () {
    let current_scroll = window.scrollY;
    
    second_mobile_searchheader_content2.style.display = "block";
    mobile_search_form2.style.display = "flex";
    mobile_search_form_input2.style.display = "block";
    mobile_search_form_cancel2.style.display = "block";

    // if (current_scroll > 190 && screen.width < 480) {
        
        se_mobile_third_header_content.style.top = "155px";
        second_mobile_searchheader_content2.style.padding = "10px 0 0 0";

    if (current_scroll > 190 && screen.width < 493) {
        se_mobile_second_header_content.style.height = "161px";
        second_mobile_searchheader_content2.style.padding = "30px 0 0 0";
    }
    // search_line_arrow.style.display = "block";
};



function cancel1 () {
    clicked = false;
    second_mobile_searchheader_content.style.display = "none";
    mobile_search_form.style.display = "none";
    mobile_search_form_input.style.display = "none";
    mobile_search_form_cancel.style.display = "none";
};



let cancel_mobile_third_header_content = document.querySelector(".mobile_third_header_content");


function cancel2 () {
    clicked = false;
    second_mobile_searchheader_content2.style.display = "none";
    mobile_search_form2.style.display = "none";
    mobile_search_form_input2.style.display = "none";
    mobile_search_form_cancel2.style.display = "none";
    cancel_mobile_third_header_content.style.top = "90px";
    se_mobile_second_header_content.style.height = "auto";
};