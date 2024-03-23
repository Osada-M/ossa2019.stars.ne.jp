"use strict";

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function popupText(popupId) {
    let copied = document.getElementById(popupId);
    // let copied = document.querySelector(popupId);
    copied.classList.add("active");
    await sleep(2000);
    copied.classList.remove("active");
}

function onClickCopy(textId, popupId){
    let target = document.getElementById(textId);
    let range = document.createRange();
    range.selectNodeContents(target);
    let selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    document.execCommand('copy');
    selection.removeAllRanges();

    popupText(popupId);
}


// タブ文字排除版（http非対応だからお蔵入り）
//
// let copyTarget = document.getElementById('copy_text').textContent;
// for(let i = 0; i < copyTarget.length; i++){
//     copyTarget = copyTarget.replace("    ", "");
// }
// for(let i = 0; i < copyTarget.length; i++){
//     copyTarget = copyTarget.replace(String.fromCharCode(160), String.fromCharCode(32));
// }
// copyTarget = copyTarget.slice(1, copyTarget.length-1)
// var clipboardText = "clipboard";
// window.clipboardData.setData("Text", clipboardText); 
// navigator.clipboard.writeText(copyTarget);
