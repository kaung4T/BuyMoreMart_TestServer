


let fp = document.querySelector(".feature_pagination");
let all_pag = fp.querySelectorAll(".pag");

let current_location = location.href;

for (let x=0;x<all_pag.length;x+=1) {

    if (all_pag[x].href == current_location) {
        all_pag[x].id = "prodcut_active";

    } 
}


let fp2 = document.querySelector(".feature_pagination2");
let all_pag2 = fp2.querySelectorAll(".pag");

let current_location2 = location.href;

for (let x=0;x<all_pag2.length;x+=1) {

    if (all_pag2[x].href == current_location2) {
        all_pag2[x].id = "prodcut_active";

    } 
}

