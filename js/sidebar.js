"use strict";

let sidebar = document.querySelector(".sidebar");
let mainContent = document.querySelector(".main_content");

// サイドバーの展開・格納
function sidebar_activate(key) {
    key.addEventListener("click", function() {
        if(sidebar.classList.contains("active")){
            sidebar.classList.remove("active");
            mainContent.classList.remove("active");
        }else{
            sidebar.classList.add("active");
            mainContent.classList.add("active");
        };
    });
}

let openBtn = document.getElementById("open_btn");
let closeBtn = document.getElementById("close_btn");
let searchBtn = document.querySelector(".bx-search");

sidebar_activate(openBtn);
sidebar_activate(closeBtn);
sidebar_activate(searchBtn);
