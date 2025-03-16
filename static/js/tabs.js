
/** @this {HTMLButtonElement & { tab: HTMLDivElement} } */
// function onTabClick(){
//     this.setAttribute("aria-selected", "true")
//     this.removeAttribute("tabindex")
//     this.tab.setAttribute("aria-hidden", "false")
//     this.tab.setAttribute("tabindex", "0")
// }

/**
 * Returns a consistent, 8 character long hash of the input string
 * @param {string} someString 
 */
const hashedConsistentId = (someString) => {
    let hash = 0;
    for (let i = 0; i < someString.length; i++) {
        const char = someString.charCodeAt(i);
        hash = ((hash << 5) - hash) + char;
        hash = hash & hash;
    }
    return hash.toString(36).substring(2, 10);
}

document.querySelectorAll('[data-is-tabs]').forEach((/** @type {HTMLDivElement} */tabGroup) => {
    if(tabGroup.classList.contains("isJSTabsProcessed")){
        return
    }
    tabGroup.classList.add("isJSTabsProcessed")
    const idPrefix = tabGroup.id || `tabs-${hashedConsistentId(tabGroup.textContent)}`;
    
    const tabsList = document.createElement('div')
    tabsList.setAttribute("role", "tablist")

    const tabs = Array.from(tabGroup.querySelectorAll('[data-tabtitle]')).map((/** @type {HTMLDivElement} */tabPanel, index) => {
        console.log(tabPanel)
        if(!tabPanel.id){
            tabPanel.id = `${idPrefix}-tab-${index}`
        }
        
        const tabName = tabPanel.dataset.tabtitle || `Tab ${index + 1}`

        const anchor = document.createElement('a')
        anchor.setAttribute("aria-controls", tabPanel.id)
        anchor.setAttribute("type", "button")
        anchor.setAttribute("role", "tab")
        anchor.setAttribute("aria-selected", "false")
        anchor.setAttribute("href", `#${tabPanel.id}`)
        anchor.id = `${idPrefix}-button-${index}`
        anchor.tab = tabPanel

        const span = document.createElement('span')
        span.textContent = tabName
        anchor.appendChild(span)
        
        tabsList.appendChild(anchor)

        tabPanel.setAttribute("aria-labelledby", anchor.id)
        tabPanel.setAttribute("role", "tabpanel")
        tabPanel.setAttribute("aria-hidden", "true")
        tabPanel.setAttribute("tabindex", "0")
        return anchor
    })

    if(tabsList.children.length === 0){
        return
    }

    let selectedTab = -1

    function setSelectedTab(currentTab, andFocus = true){
        if(currentTab === selectedTab){
            return
        }
        selectedTab = currentTab
        tabs.forEach((tab, index) => {
            if(index === currentTab){
                tab.setAttribute("aria-selected", "true")
                tab.removeAttribute("tabindex")
                tab.tab.setAttribute("aria-hidden", "false")
                if(andFocus){
                    tab.tab.focus()
                }
            } else {
                tab.setAttribute("aria-selected", "false")
                tab.setAttribute("tabindex", "-1")
                tab.tab.setAttribute("aria-hidden", "true")
            }
        })
    }

    function setNextTab(){
        setSelectedTab((selectedTab + 1) % tabs.length)
    }

    function setPreviousTab(){
        setSelectedTab((selectedTab + tabs.length - 1) % tabs.length)
    }

    tabGroup.addEventListener("keydown", event => {
        if(event.key === "ArrowRight" || event.key === "ArrowDown"){
            setNextTab()
        } else if(event.key === "ArrowLeft" || event.key === "ArrowUp"){
            setPreviousTab()
        }else if(event.key === "Home"){
            setSelectedTab(0)
        }
        else if(event.key === "End"){
            setSelectedTab(tabs.length - 1)
        }
    })

    function onTabClick(event){
        setSelectedTab(tabs.indexOf(event.currentTarget))
        event.preventDefault()
        history.pushState({}, "", this.href);
    }

    tabs.forEach(tab => tab.addEventListener("click", onTabClick))

    const hash = window.location.hash
    const tabIndex = hash !== "" && tabs.findIndex(tab => tab.getAttribute("href") === hash)
    setSelectedTab(tabIndex !== false && tabIndex !== -1 ? tabIndex : 0, false)

    tabGroup.prepend(tabsList)
})