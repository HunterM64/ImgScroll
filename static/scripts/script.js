x = 1

function clickFunction(element) {
    console.log(element.className);
    if(element.className == "image") {
        element.className = "overlay";
        document.getElementById("void").style.display = "block";
    } else {
        element.className = "image";
        document.getElementById("void").style.display = "none";
    }
        
}