window.onload = function() {
    let button = document.getElementById('nav-button')
    let nav = document.getElementById('nav')

    button.onclick = function(e) {
        if(nav.style.display==="block") {
            nav.style.display = "none"
        } else {
            nav.style.display = "block"
        }
    }
}