const KMPERMILE = 1.60934;


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