"use strict";

fetch("../count/count.txt")
  .then(res=>res.text())
  .then(text=>document.getElementById("counter").textContent=text);
