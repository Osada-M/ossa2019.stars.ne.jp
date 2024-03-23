"use strict";

function count(){
    const xs = document.getElementById("textArea").value;
    let len = xs.length;
    console.log(xs, len);
    for(let i = len; i--;){
        if(xs[i] === "\n"){
            len--;
        }
    }
    document.getElementById("count_number").innerText = len;
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function popupText(popupId) {
    let copied = document.getElementById(popupId);
    copied.classList.add("active");
    await sleep(2000);
    copied.classList.remove("active");
}

function onClickCopy_textCounter(textId, popupId) {
    const copyTarget = document.getElementById(textId);
    copyTarget.select();
    document.execCommand("copy");

    popupText(popupId);
}

function shift(popupId) {
    event.preventDefault();
    const before = document.getElementById("before").value;
    const after = document.getElementById("after").value;
    const xs = document.getElementById("textArea").value;
    document.getElementById("textArea").value = xs.split(before).join(after);
    // document.getElementById("output").innerHTML = before+"を"+after+" に置換しました！";

    popupText(popupId);
}