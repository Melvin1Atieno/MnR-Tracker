// modal script

// get button that opens modal
var btnA = document.getElementById("Abtlink");

var btnS = document.getElementById("Slink");

// get  services modal
var modalS = document.getElementById("SModal")

// get about modal
var modalAbt = document.getElementById("AbtModal");

//get span element that closes About moadal
var span = document.getElementsByClassName("close");

// get the span element that closes the services modal
// var Sspan = document.getElementsByClassName("close")[1];



// About modal functions

// open About modal on click
btnA.onclick = function(){
    modalAbt.style.display="block";
}
//  close the about modal when span element is clicked
span[0].onclick = function() {
    modalAbt.style.display ="none";

}


// open service modal functions
btnS.onclick = function () {
    modalS.style.display = "block";
}
//  close the about modal when span element is clicked
span[1].onclick = function () {
    modalS.style.display = "none";

}
