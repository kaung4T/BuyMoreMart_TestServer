



let current = location.href;

let v = document.querySelector('.third_header');
let all = v.querySelectorAll('a');

for (var num=0;num<all.length;num++) {
    if (all[num].href == current) {
        all[num].className = 'active';
    } 
}

// mobile

let mv = document.querySelector('.mobile_third_header');
let mall = mv.querySelectorAll('a');

for (var num=0;num<mall.length;num++) {
    if (mall[num].href == current) {
        mall[num].className = 'active';
    } 
}

// tablet

let tv = document.querySelector('.tablet_third_header');
let tall = tv.querySelectorAll('a');

for (var num=0;num<tall.length;num++) {
    if (tall[num].href == current) {
        tall[num].className = 'active';
        
    } 
}

