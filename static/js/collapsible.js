document.querySelectorAll('button[aria-expanded="true"][aria-controls]').forEach((/** @type {HTMLButtonElement} */button) => {
    if(button.classList.contains("isJSProcessed")){
        return
    }
    button.classList.add("isJSProcessed")
    const target = document.getElementById(button.getAttribute('aria-controls'));
    if(!target){ 
        return;
    }
    button.addEventListener('click', () => {
        const expanded = button.getAttribute('aria-expanded') === 'true';
        button.setAttribute('aria-expanded', expanded ? 'false' : 'true');
        target.setAttribute('aria-hidden', expanded ? 'true' : 'false');
    });

    if(button.dataset.close === "true"){
        button.click()
    }
})