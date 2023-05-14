


let profile_current = location.href;

let profile_left = document.querySelector(".profile_left");
let profile_ul = profile_left.querySelector("ul");
let profile_li = profile_ul.querySelectorAll("li");

let profile_a= profile_left.querySelectorAll("a");




for (var num=0;num<profile_a.length;num++) {

    if (profile_a[num].href == profile_current) {
        profile_li[num].className = 'profile_left_active';
    }

}



