"use strict";

function efffect_0(serector){
    document.querySelector(serector).onmousemove = (e) => {
        const x = e.pageX - e.target.offsetLeft
        const y = e.pageY - e.target.offsetTop
        e.target.style.setProperty('--x', `${ x }px`)
        e.target.style.setProperty('--y', `${ y }px`)
    }
}

// effect_0(".pointer_effect_0");
