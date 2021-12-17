
import {removeDiv, getDiv, setTitle, createImageButtonOnDiv} from "./helpers.js"
import {troops, Character} from "./objects.js"
import {classes} from "./classes.js"

//Constantes Exportaveis
export var characterClass = Object.entries(new Character("Hiro", classes["villager"]))
export const hostileEntities = Object.entries(troops.enemies)
export const classList = Object.entries(classes)
//Buttons

var classButton = document.querySelector("button#classStatus")
classButton.addEventListener("click", showClass, false)

var resetButton = document.querySelector("button#resetPageLayout")
resetButton.addEventListener("click", removeDiv, false)

var enemiesButton = document.querySelector("button#enemiesList")
enemiesButton.addEventListener("click", showEnemies, false)

var chooseClassButton = document.querySelector("button#chooseClass")
chooseClassButton.addEventListener("click", listClasses, false)

document.addEventListener("DOMContentLoaded", function() {
    console.log("loaded")
}, false)
//functions

export function showClass(){
    removeDiv()
    let div = getDiv("status")
    setTitle(div, `Player Status`)
    for (let keyValue of characterClass){
        if(keyValue[0] === "src"){ continue}
        listInformation(div, keyValue)
        
    }
}

export function listInformation(div, informationList){
    let para = document.createElement('p')
    var att, val
    att = informationList[0][0].toUpperCase() + informationList[0].slice(1)
    val = String(informationList[1])
    let text = document.createTextNode(`${att}: ${val}`)
    para.appendChild(text)
    div.appendChild(para)
}

export function showEnemies(){
    removeDiv()
    let div = getDiv("status")
    setTitle(div, "Enemies")
    for (let x = 0; x < hostileEntities.length; x++){
        for (let y = 1; y < hostileEntities[x].length; y++){
            var obj = hostileEntities[x][y];
            let objects = Object.entries(obj)
            for (let z = 0; z < objects.length; z++){
                listInformation(div, objects[z])
            }
        }
    }
}

export function listClasses(){
    removeDiv()
    var div = getDiv("classes")
    setTitle(div, "Choose a Class")
    
    for (let Class of classList){
        createImageButtonOnDiv(div, Class[1]["classname"], Class[1]["classname"] + "-class", Class[1]["src"])
    }       
}

export function changeClassTo(evt){
    console.log(evt.currentTarget.classname)
}




