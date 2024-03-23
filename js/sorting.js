"use strict";


const sleep = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// 棒グラフを表示（now_index = 赤色で表示するもの）
const plot_bar = (arr, now_index, active) => {
    let index = 0;
    for (let element of bar) {
        if (index >= arr.length){
            break;
        }
        if (index == now_index && active) {
            bar[index].style.background = "#f11";
        } else {
            bar[index].style.background = "#555";
        }
        element.style.height = ((arr[index++] + 1)*HEIGHT_COF) + "px";
    }
}

// 赤色のバーを表示 or 全非表示
const red_bar = (index, active) => {
    for (let i=0; i<RANGE; i++){
        if (i == index && active) {
            bar[i].style.background = "#f11";
        } else {
            bar[i].style.background = "#555";
        }
    }
}

// 配列のシャッフル
async function shuffle([...arr]) {
    for (let i=0; i<=arr.length - 1; i++) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
        plot_bar(arr, i, true);
        await sleep(10);
    }
    data = arr;
    red_bar(0, false);
}

// シャッフルを実行
const clickToShuffle = () => {
    if(!be_sorting_now){
        shuffle(data);
        was_sort = false
        be_sorting_now = false;
    }
};

// ソートを実行
const clickToSort = (kind) => {
    if (!was_sort) {
        if (kind == "bubble") {
            was_sort = true;
            be_sorting_now = true;
            bubbleSort(data);
        } else if (kind == "merge") {
            was_sort = true;
            be_sorting_now = true;
            mergeSort(data);
        } else if (kind == "quick") {
            was_sort = true;
            be_sorting_now = true;
            quickSort(data);
        }
    }
};

// バブルソート
async function bubbleSort([...arr]) {
    let tmp;
    for (let i=arr.length-1; i>=0; i--) {
        for (let j = 0; j < i; j++ ) {
            if (arr[j] > arr[j+1]) {
                tmp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = tmp;
            }
            plot_bar(arr, j+1, true);
            await sleep(speed);
        }
    }
    data = arr;
    red_bar(0, false);
    be_sorting_now = false;
}

// マージソート
async function mergeSort(arr) {
    let sorted = arr.slice();
    let n = sorted.length;
    let buffer = new Array(n), plot_buffer = new Array(n);
    let left, right, leftLimit, rightLimit, i, temp;

    for (let size=1; size<n; size*=2) {
        for (let leftStart=0; leftStart<n; leftStart+=2*size) {
            left = leftStart;
            right = Math.min(left + size, n);
            leftLimit = right;
            rightLimit = Math.min(right + size, n);
            i = left;
            while (left < leftLimit && right < rightLimit) {
                if (sorted[left] <= sorted[right]) {
                    buffer[i++] = sorted[left++];
                } else {
                    buffer[i++] = sorted[right++];
                }
            }
            for (let j=0; j<RANGE; j++){
                if(plot_buffer[j] != buffer[j] && buffer[j] != undefined){
                    plot_buffer[j] = buffer[j]
                    plot_bar(plot_buffer, j, true);
                    await sleep(speed);
                }
            }
            while (left < leftLimit) {
                buffer[i++] = sorted[left++];
            }
            for (let j=0; j<RANGE; j++){
                if(plot_buffer[j] != buffer[j] && buffer[j] != undefined){
                    plot_buffer[j] = buffer[j]
                    plot_bar(plot_buffer, j, true);
                    await sleep(speed);
                }
            }
            while (right < rightLimit) {
                buffer[i++] = sorted[right++];
            }
            for (let j=0; j<RANGE; j++){
                if(plot_buffer[j] != buffer[j] && buffer[j] != undefined){
                    plot_buffer[j] = buffer[j]
                    plot_bar(plot_buffer, j, true);
                    await sleep(speed);
                }
            }
        }
        temp = sorted;
        sorted = buffer;
        buffer = temp;
    }

    plot_bar(sorted, 0, false);
    data = sorted;
    be_sorting_now = false;
}

// クイックソート  
async function quickSort(arr) {
    let stack = [];
    let start = 0;
    let end = arr.length - 1;
    let pivot, i, temp;
    stack.push({low: start, high: end});
    while(stack.length){
        const {low, high} = stack.shift();
        pivot = arr[high];
        i = low;
        for(let j = low; j < high; j++){
            if(arr[j] <= pivot){
                plot_bar(arr, i, true);
                await sleep(speed);
                swap(arr, i, j);
                plot_bar(arr, j, true);
                await sleep(speed);
                i++;
            }
        }
        swap(arr, i, high);
        if(i - 1 > low){
            stack.push({low: low, high: i - 1});
            plot_bar(arr, high, true);
            await sleep(speed);
        }
        if(i + 1 < high){
            stack.push({low: i + 1, high: high});
            plot_bar(arr, low, true);
            await sleep(speed);
        }
    }
    plot_bar(arr, i, true);
    await sleep(speed);
    red_bar(0, false);
    data = arr;
    be_sorting_now = false;
}
const swap = (arr, left, right) =>  {
    const temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp;
}


// シミュレートの速度を設定
const getSpeed = (number) => {
    let speed_buffer = MAX_SPEED - Math.floor(number * SPEED_COF);
    document.getElementById("speed_number").textContent = number.toString();
    return speed_buffer;
}

const getSliderValue = (e) => {
    input_number = e.target.value;
    speed = getSpeed(input_number);
}

const smooth_activate = () => {
    let bar = document.querySelector(".bar_content");
    let btn = document.getElementById("smooth_btn");
    if(btn.classList.contains("active")){
        bar.classList.remove("active");
        btn.classList.remove("active");
    }else{
        bar.classList.add("active");
        btn.classList.add("active");
    }
    if(!be_sorting_now){
        clickToShuffle();
    }
}

const input_slider = document.getElementById("speed_slider");

const RANGE = 40;
const HEIGHT_COF = 15;
const MAX_SPEED = 200;
const SPEED_COF = MAX_SPEED / 100;

let speed = getSpeed(80);
let input_number;

const bar = document.getElementsByClassName("bar");
let data = [...Array(RANGE).keys()];
let was_sort = false;
let be_sorting_now = false;
let red_activateList = Array.from(Array(RANGE), () => 0);

window.onload = () => {
    input_slider.addEventListener('input', getSliderValue);
}

clickToShuffle();
