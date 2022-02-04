export function removeDiv(exceptionDiv){
    var divsToRemove = document.querySelectorAll(".dynamicCreated")
    var divsToHide = document.querySelectorAll(".seen")
    var divsToClear = document.querySelectorAll(".clearable")
    var divsToErase = document.querySelectorAll("div#screen > img")
    var divIdlist = []


    //Selecionando divs para apagar
    for (let value of Object.values(divsToRemove)){
        console.log("Value of divsToRemove: " + value.id)
        let divId = String(value.id)

        if (divId === ""){
            continue
        }
        if (exceptionDiv !== ""){
            if (divId === exceptionDiv){
                continue
                
            }
        }
       

        let divQuery = `#` + divId
        divIdlist.push(divQuery)
        console.log(divIdlist)

    }

    //Selecionando divs para esconder

    for (let value of Object.values(divsToHide)){
        console.log("values: " + value.id)
        document.querySelector(`#${value.id}`).setAttribute("class", "hidden")
    }

    for (let value of Object.values(divsToClear)){
        console.log("values: " + value.id)
        document.querySelector(`#${value.id}`).remove()
    }
    for (let y of divIdlist){
        document.querySelector(y).remove()
    }

    for (let y of divsToErase){
        console.log("values: " + y.id)
        document.querySelector(`#${y.id}`).remove()
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
    if (locator === null) {
        var division = document.createElement('div')
        var id = document.createAttribute('id')
        var group = document.createAttribute('class')
        if (cssClass === undefined){
            group.value = "dynamicCreated"
           
        } else{
            group.value = cssClass
        }
        id.value = idv
        division.setAttributeNode(id)
        division.setAttributeNode(group)
        document.body.appendChild(division)
        var div = document.querySelector(query)
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

export function createImageButtonOnDiv( name, id, image){
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
    return aDiv
    
    
}

export function singleSimpleMessage(div, msg){
    let para = document.createElement('p')
    let txt = document.createTextNode(msg)
    para.appendChild(txt)
    div.appendChild(para)
}

export function sleep(milliseconds) {  
    //eslint-disable-next-line no-promise-executor-return
    return new Promise((resolve) => setTimeout(resolve, milliseconds));  
 }

export function callTestSpace(){

    let space = getDiv("TestingSpace")
    return space
}

export function testSubject(){

    let testSpace = callTestSpace();

    document.addEventListener("keydown", function(evnt){
        if (evnt.key === "Shift"){
            let text = document.createTextNode("Shifted")
            let para = document.createElement("para")
            para.appendChild(text)
            testSpace.appendChild(para)
        }
    } )


}   
