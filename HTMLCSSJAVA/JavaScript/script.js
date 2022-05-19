const KMPERMILE = 1.60934;
const PPERD = 1.24;


function resetdistances() {
    var m = document.getElementById("miles");
    var km = document.getElementById("kms");
    m.value = "";
    km.value = "";
}


function miles2kms() {
    var m = document.getElementById("miles");
    var km = document.getElementById("kms");
    km.value = (m.value * KMPERMILE).toFixed(2)
    // alert(mValue+"m in km = "+kmValue)
    // console.log("in miles2kms() = "+kmValue)
}


function kms2miles() {
    var m = document.getElementById("miles");
    var km = document.getElementById("kms");
    m.value = (km.value/KMPERMILE).toFixed(2)
    // alert("in kms2miles()")
    // console.log("in kms2miles()")
}

function ptod(){
    var p = document.getElementById("pounds")
    var d = document.getElementById("dollars")
    d.value = (p.value*PPERD).toFixed(2)
}

function dtop(){
    var p = document.getElementById("pounds")
    var d = document.getElementById("dollars")
    p.value = (d.value/PPERD).toFixed(2)
}