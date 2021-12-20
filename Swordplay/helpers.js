export function removeDiv(exceptionDiv){
    var divsToRemove = document.querySelectorAll("div.dynamicCreated")
    var divsToHide = document.querySelectorAll("div.seen")
    var divsToClear = document.querySelectorAll("div.clearable")
    var divIdlist = []


    //Selecionando divs para apagar
    for (let index in Object.keys(divsToRemove)){
        let divId = String(Object.entries(divsToRemove)[index][1].id)

        if (divId === ""){
            continue
        }
        if (exceptionDiv !== ""){
            if (divId === exceptionDiv){
                continue
                
            }
        }
       

        let divQuery = `div#` + divId
        divIdlist.push(divQuery)
        console.log(divIdlist)

    }

    //Selecionando divs para esconder

    for (let value of Object.values(divsToHide)){
        console.log("values: " + value.id)
        document.querySelector(`div#${value.id}`).setAttribute("class", "hidden")
    }

    for (let value of Object.values(divsToClear)){
        console.log("values: " + value.id)
        document.querySelector(`div#${value.id}`).remove()
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

export function getDiv(idv, cssClass){
    var query = `div#${idv}`
    console.log(`div#${idv} of class ${cssClass}`)
    var locator = document.querySelector(query)
    if (locator == null) {
        var division = document.createElement('div')
        var id = document.createAttribute('id')
        var group = document.createAttribute('class')
        if (cssClass !== undefined){
            group.value = cssClass
        } else{
            group.value = "dynamicCreated"
        }
        id.value = idv
        division.setAttributeNode(id)
        division.setAttributeNode(group)
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
    let aDiv = getDiv(id + "input", "clearable")
    let para = document.createElement("p")
    let input = document.createElement("input")
    let clssname = document.createTextNode(" - " + name)
    let inputType = document.createAttribute("type")
    let src = document.createAttribute('src')
    let idv = document.createAttribute("id")
    let bid = document.createAttribute("id")
    let classname = document.createAttribute("name")

    let Value = image
    classname.value = name.toLowerCase()
    inputType.value = "Image"
    src.value = Value
    idv.value = id
    bid.value = name + "-bid"

    para.appendChild(clssname)
    input.setAttributeNode(bid)
    input.setAttributeNode(classname)
    input.setAttributeNode(inputType)
    input.setAttributeNode(idv)
    input.setAttributeNode(src)
    aDiv.appendChild(input)
    aDiv.appendChild(para)
    div.appendChild(aDiv)
    
    
}

export function singleSimpleMessage(div, msg){
    let para = document.createElement('p')
    let txt = document.createTextNode(msg)
    para.appendChild(txt)
    div.appendChild(para)
}

export function sleep(milliseconds) {  
    return new Promise(resolve => setTimeout(resolve, milliseconds));  
 } 