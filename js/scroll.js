"use strict";

// 画面上までスクロール
let vGoTop = {};
function tmTopScroll(){

	vGoTop["coef"] = 50;
	vGoTop["cnt"]  = 0;

	let startX = document.body.scrollLeft || document.documentElement.scrollLeft;
	let startY = document.body.scrollTop  || document.documentElement.scrollTop;

	let moveSplitCnt = 0;
	for(let i = 1; i <= vGoTop["coef"]; i++) {
		moveSplitCnt += i * i;
	}
	vGoTop["unitH"] = startY / ( moveSplitCnt * 2 );

	vGoTop["nextX"] = startX;
	vGoTop["nextY"] = startY;

	tmTopScrollLoop();
}
function tmTopScrollLoop(){
	vGoTop["cnt"]++;

	let Coef = 0;
	if(vGoTop["cnt"] <= vGoTop["coef"]){
		Coef = vGoTop["cnt"];
	}else{
		Coef = ((vGoTop["coef"] * 2) + 1) - vGoTop["cnt"];
	}
	vGoTop["nextY"] = vGoTop["nextY"] - Math.round( vGoTop["unitH"] * ( Coef * Coef) );
	if((vGoTop["cnt"] >= (vGoTop["coef"] * 2))||(vGoTop["nextY"] <= 0)){
		vGoTop["nextY"] = 0;
	}

	window.scrollTo(vGoTop["nextX"], vGoTop["nextY"]);

	if(vGoTop["nextY"] <= 0){
		clearTimeout(vGoTop["timer"]);
	}else{
		vGoTop["timer"] = setTimeout("tmTopScrollLoop()",10);
	}
}
