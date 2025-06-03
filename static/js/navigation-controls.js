// Toggle adding the "-open" variant to the mobile menu button in the main navigation bar
function navToggleMenu(navElement) {
  navElement.classList.toggle("-open");
}

var navTutorialLinks = document.getElementsByClassName("menu-link", "-section");

// Toggles links visible in the side menu
function navTutorialToggleSection(menuLink) {
  menuLink.nextElementSibling.classList.toggle("-folded");
}

document.addEventListener("DOMContentLoaded", () => {
  if (navTutorialLinks.length > 0) {
    const menuLink = navTutorialLinks[0];
    if (menuLink.nextElementSibling.classList.contains("-folded")) {
      menuLink.click();
    }
  }
});

// Toggles the tutorial menu, altering the overflow of <body>
function navTutorialMobileToggle(closeButton) {
  if (document.body.style.overflowY === "") {
    document.body.style.overflowY = "hidden";
  } else {
    document.body.style.overflowY = "";
  }
  closeButton.previousElementSibling.classList.toggle("-open");
}
