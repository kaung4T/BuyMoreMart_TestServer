



let dropdown = document.querySelector(".dropdown");
let drop_menu = dropdown.querySelector(".dropdown-menu");


dropdown.addEventListener("click", clicker);


function clicker () {
    drop_menu.style.display = "flex";
    drop_menu.style.flexWrap = "wrap";
};