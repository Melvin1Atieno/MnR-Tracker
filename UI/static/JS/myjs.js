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

// function to open sidenav
function openNav (){
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft="250px";


    // functionto close sidenav
}
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
}

// function to display requests
function displayrequests() {
    // document.getElementById("userTable").style.display = "none";
    document.getElementById("myTable").style.display = "block";
    document.getElementById("tableheading").style.display = "block";
    document.getElementById("dashboard").style.display="none";
}
// function to display dashboard
function displaydashboard(){
    document.getElementById("dashboard").style.display="flex";
    // document.getElementById("userTable").style.display = "none";
    document.getElementById("myTable").style.display = "none";
    // document.getElementById("tableheading").style.display = "none";

}
// filter search function

function filterFunction() {
    var input, filter, table, tr,td, i;
    input = document.getElementById("fInput");
    filter = input.Value.toUpperCase();
    table= document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    for( i = 0; i< tr.length; i++){
        td = tr[i].getElementByTageName("td")[0];
        if(td){
            if
            (td.innerHTML.toUpperCase().indexOf(filter)> -1){
                tr[i].style.display=""
            }
            else 
            {
                tr[i].style.display ="none"
            }
            
        }
    }
}

// function to display users
// function displayUsers(){
//     document.getElementById("userTable").style.display="block";
//     document.getElementById("myTable").style.display = "none";
//     document.getElementById("dashboard").style.display = "none";

// }
// function to display logout modal
// get modal
var Lmodal = document.getElementById("LModal");
function displayLogout(){
    Lmodal.style.display="block";
}
span[2].onclick = function() {
  Lmodal.style.display = "none";
}