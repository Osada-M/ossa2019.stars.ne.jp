"use strict";

function fade(target, start, end){
    $(target).append(
        "<style>" + target + "{display:none;}"
    );
    $(window).on("load", function() {
        $(target).delay(start).fadeIn(end);
    });
}

const mono = 150;

fade("#fade_0", 0, 500);
fade("#fade_1", mono, 500);
fade("#fade_2", mono*2, 500);
fade("#fade_3", mono*3, 500);
fade("#fade_4", mono*4, 500);
fade("#fade_5", mono*5, 500);
fade("#fade_6", mono*6, 500);
fade("#fade_7", mono*7, 500);
fade("#fade_8", mono*8, 500);
fade("#fade_9", mono*9, 500);
fade("#fade_10", mono*10, 500);
fade("#fade_11", mono*11, 500);
fade("#fade_12", mono*12, 500);
fade("#fade_13", mono*13, 500);
fade("#fade_14", mono*14, 500);
fade("#fade_15", mono*15, 500);
fade("#fade_16", mono*16, 500);
fade("#fade_17", mono*17, 500);
fade("#fade_18", mono*18, 500);
fade("#fade_19", mono*19, 500);
fade("#fade_20", mono*20, 500);
fade("#fade_21", mono*21, 500);
fade("#fade_22", mono*22, 500);
fade("#fade_23", mono*23, 500);
fade("#fade_24", mono*24, 500);
fade("#fade_25", mono*25, 500);
fade("#fade_26", mono*26, 500);
fade("#fade_27", mono*27, 500);
fade("#fade_28", mono*28, 500);
fade("#fade_29", mono*29, 500);
fade("#fade_default", 500, "slow");
