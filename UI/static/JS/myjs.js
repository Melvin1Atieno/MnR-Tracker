// About modal script
// get modal
var modal = document.getElementById("AbtModal");

// get button that opens modal
var btn = document.getElementById("Abtlink");

//get span element that closes moadal
var span = document.getElementsByClassName("close")[0];


// open on click
btn.onclick = function (){
    modal.style.display = "block";
}

//  close when span element is clicked
span.onclick = function() {
    modal.style.display ="none";

}
// closes modal when user clicks anywhere ouside modal
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none"
    }
}
