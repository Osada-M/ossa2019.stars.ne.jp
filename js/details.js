"use strict";

// 折り畳み欄の展開・格納
function details_activate(target){
    let detailsWindow = document.getElementById(target);
    if(detailsWindow.classList.contains("active")){
        detailsWindow.classList.remove("active");
    }else{
        detailsWindow.classList.add("active");
    };
}
