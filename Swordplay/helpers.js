export function removeDiv(){
    var Divs = document.getElementsByTagName("div")
    console.log(Object.entries(Divs))
    var divIdlist = []
    for (let index in Object.keys(Divs)){
        console.log(index, Object.keys(Divs))
        let divId = String(Object.entries(Divs)[index][1].id)
        if (divId === ""){
            continue
        }
        let divQuery = `div#` + divId
        divIdlist.push(divQuery)
        console.log(divIdlist)

    }
    for (let y of divIdlist){
        document.querySelector(y).remove()
    }
    
}
export function setTitle(div, title){
    let para = document.createElement('h2')
    let text = document.createTextNode(`${title}`)
    para.appendChild(text)
    div.appendChild(para)
}

export function getDiv(idv){
    var query = `div#${idv}`
    var locator = document.querySelector(query)
    if (locator == null) {
        var division = document.createElement('div')
        var id = document.createAttribute('id')
        id.value = idv
        division.setAttributeNode(id)
        document.body.appendChild(division)
        var div =  document.querySelector(query)
        return div
    } else {
        locator.innerHTML = ""
        console.log("div Cleared")
        return locator
    }
}

export function origin(){
    let urlOrigin = location.origin
    let fileOrigin = location.pathname
    let hrefOrigin = location.href
    console.log(urlOrigin, fileOrigin, hrefOrigin)
}

export function createImageButtonOnDiv(div, name, id, image){
    let aDiv = getDiv(id + "button")
    let para = document.createElement("p")
    let buttonReal = document.createElement("button")
    let clssname = document.createTextNode(" - " + name)
    let anButton = document.createElement('img')
    let src = document.createAttribute('src')
    let idv = document.createAttribute("id")
    let bid = document.createAttribute("id")
    let alt = document.createAttribute('al')
    let Value = image
    alt.value = name
    src.value = Value
    idv.value = id
    bid.value = name + "-bid"
    para.appendChild(clssname)
    buttonReal.setAttributeNode(bid)
    anButton.setAttributeNode(idv)
    anButton.setAttributeNode(alt)
    anButton.setAttributeNode(src)
    buttonReal.appendChild(anButton)
    aDiv.appendChild(buttonReal)
    aDiv.appendChild(para)
    div.appendChild(aDiv)
    
    
}