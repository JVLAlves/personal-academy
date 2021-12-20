
import {removeDiv, getDiv, setTitle, createImageButtonOnDiv, singleSimpleMessage, sleep} from "./helpers.js"
import {troops, Player, enemyRoulette} from "./objects.js"
import {classes} from "./classes.js"

//Constantes Exportaveis
export const hostileEntities = Object.entries(troops.enemies)
export const classList = Object.entries(classes)
//Buttons
export var character = new Player("Hiro", )
window.character = character
document.body.addEventListener("click", function(evt){
    switch (true){
        case evt.target.matches("button#classStatus"):
            document.querySelector("button#classStatus").addEventListener("click",
            showClass(), false)
            break
        case evt.target.matches("button#resetPageLayout"):
            document.querySelector("button#resetPageLayout").addEventListener("click",
            removeDiv(), false)
            break
        case evt.target.matches("button#enemiesList"):
            document.querySelector("button#enemiesList").addEventListener("click",
            showEnemies(), false)
      
            break
        case evt.target.matches("button#chooseClass"):
            document.querySelector("button#chooseClass").addEventListener("click",
            listClasses(), false)
        case evt.target.matches("div#classListToChoose"):
         document.querySelector("div#classListToChoose").addEventListener("click",
        function(evnt){
            if (evnt.target.matches("Input")){changeClassTo(evnt.target.name)}
        }, false)
            break
        case evt.target.matches("button#starting"):
            document.querySelector("button#starting").addEventListener("click", battle(), false)
}}, false)


//functions
export function showClass(){
    removeDiv()
    let div = getDiv("status")
    setTitle(div, `Player Status`)
    let charClass = character.class
    if (charClass === undefined){
        singleSimpleMessage(div, "You must choose a class first")
        var sButton = document.querySelector("button#chooseClass")
        sButton.setAttribute("class", "doHighlight")
        return
    } else{
    for (let keyValue of Object.entries(character.class)){
        if(keyValue[0] === "src"){ continue}
        listInformation(div, keyValue)
        
        }
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
    var div = document.querySelector("div#classListToChoose")
    for (let Class of classList){
        createImageButtonOnDiv(div, Class[1]["classname"], Class[1]["classname"] + "-class", Class[1]["src"])
    }
    div.setAttribute("class", "seen")
}

export function changeClassTo(classname){
    let oldClass 
    if (character.class !== undefined){
   oldClass = character.class.classname}
    character.class = classes[classname]
    if (oldClass !== "" && oldClass === character.class.classname){
        console.log("You've already choose this class.")
    } else if (oldClass !== "" && oldClass !== character.class.class){ console.log(`Your previous class ${oldClass} was changed to ${character.class.classname}`)} else{
        console.log(`You've chosen the class ${classname}. Good Luck!`)
    }
  

}

export async function battle(){
    //clearing
    removeDiv()

    //verifying
     
    let charClass = character.class
    if (charClass === undefined){
        let div = getDiv("Alert")
        singleSimpleMessage(div, "You must choose a class first")
        var sButton = document.querySelector("button#chooseClass")
        sButton.setAttribute("class", "doHighlight")
        return
    }

    //Setting entities information
    console.log("Setting Thing Up")
    let gameScreen = document.querySelector("div#screen")
    let chosenEnemy = enemyRoulette()
    console.log(chosenEnemy)
    gameScreen.setAttribute("class", "seen")
    var PlayerName = character.nickname
    var playerLife = Number.parseInt(character.class.health)
    var playerDmg = Number.parseInt(character.class.damage)

    let plyrHp = document.querySelector("p#player")
    let enemHp = document.querySelector('p#enemy')

    var enemyName = chosenEnemy.classname
    var enemyLife = Number.parseInt(chosenEnemy.health)
    var enemyDmg = Number.parseInt(chosenEnemy.damage)

    //Battle Begin
    console.log("Starting Battle")
    
    let c = 0
    while (true){
        console.log(`Round ${c}`)
        let playerTextContent = `${PlayerName}: ${playerLife}`
        let enemyTextContent = `${enemyName}: ${enemyLife}`
        plyrHp.innerHTML = playerTextContent
        enemHp.innerHTML = enemyTextContent
        playerLife -= enemyDmg
        enemyLife -= playerDmg

        if (playerLife <= 0 || enemyLife <= 0){
            let playerTextContent = `${PlayerName}: ${playerLife}`
            let enemyTextContent = `${enemyName}: ${enemyLife}`
            plyrHp.innerHTML = playerTextContent
            enemHp.innerHTML = enemyTextContent
            if (playerLife <= 0){
                let loseMessage = document.querySelector("p#lost")
                loseMessage.setAttribute("class", "seen")
                return
            } else if (enemyLife <= 0){
                let wonMessage = document.querySelector("p#won")
                wonMessage.setAttribute("class", "seen")
                return
            }
        }
        c++
        await sleep(1500)

    }
}




