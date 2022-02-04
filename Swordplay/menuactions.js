/*eslint-disable max-lines */

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
            break
        case evt.target.matches("div#classListToChoose"):
         document.querySelector("div#classListToChoose").addEventListener("click",
        function(evnt){
            if (evnt.target.matches("Input")){changeClassTo(evnt.target.name)}
        }, false)
            break
        case evt.target.matches("button#starting"):
            document.querySelector("button#starting").addEventListener("click", Showdown(), false)
        break
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
        div.appendChild(createImageButtonOnDiv(Class[1]["classname"], Class[1]["classname"] + "-class", Class[1]["src"]))
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
    document.querySelector("p#lost").setAttribute("class", "hidden")
    document.querySelector("p#won").setAttribute("class", "hidden")

    //verifying
    let charClass = character.class
    if (charClass === undefined){
        let div = getDiv("Alert")
        singleSimpleMessage(div, "You must choose a class first")
        var sButton = document.querySelector("button#chooseClass")
        sButton.setAttribute("class", "doHighlight")
        return
    }

    //Setting Screen information
    console.log("Setting Thing Up")
    let gameScreen = document.querySelector("div#screen")
    gameScreen.setAttribute("class", "seen")
    let plyrHp = document.querySelector("p#player")
    plyrHp.setAttribute("class", "seen")
    let enemHp = document.querySelector('p#enemy')

    console.log(character.class)

    var player = {

        "name": character.nickname,
        "health": Number.parseInt(character.class.health),
        "dmg": Number.parseInt(character.class.damage),
        damageBuff: async function(){
            document.addEventListener("keydown",function(evt){
                if (evt.key === "Shift" && player.damageBuffUsages > 0 ){
                    document.querySelector("p#player").setAttribute("class", "dmgUP")
                    player.dmg += 20
                    player.damageBuffUsages -= 1
                    console.log("Dmg +Up", `Usages: ${player.damageBuffUsages}`)
                }
            }, false)},
        "damageBuffUsages": 3

    }

    const ChosenEnemy = enemyRoulette()

    var enemy = {
        "name": ChosenEnemy.classname,
        "health": Number.parseInt(ChosenEnemy.health),
        "dmg": Number.parseInt(ChosenEnemy.damage),
        taunt: function(){console.log("Hello!")},
    }

    //Battle Begin
    console.log("Starting Battle")
    
    let c = 0
    while (true){
        //looping configs

        //Interface Changes
        console.log(`Round ${c}`)
        let playerTextContent = `${player.name}: ${player.health}`
        let enemyTextContent = `${enemy.name}: ${enemy.health}`
        plyrHp.innerHTML = playerTextContent
        enemHp.innerHTML = enemyTextContent

        //Numbers changes
        player.damageBuff()
        console.log(player.dmg)
        player.health -= enemy.dmg
        enemy.health -= player.dmg
        enemy.taunt()

        //End Verification
        if (player.health <= 0 || enemy.health <= 0){
            let playerTextContent = `${player.name}: ${player.health}`
            let enemyTextContent = `${enemy.name}: ${enemy.health}`
            plyrHp.innerHTML = playerTextContent
            enemHp.innerHTML = enemyTextContent
            if (player.health <= 0){
                let loseMessage = document.querySelector("p#lost")
                loseMessage.setAttribute("class", "seen")
                return
            } else if (enemy.health <= 0){
                let wonMessage = document.querySelector("p#won")
                wonMessage.setAttribute("class", "seen")
                return
            }
        }

        c++ //Round counter
        await sleep(1500) //End of the Round interval

    }

}


export async function Showdown(){
    //clearing
    removeDiv()
    document.querySelector("p#lost").setAttribute("class", "hidden");
    document.querySelector("p#won").setAttribute("class", "hidden");
    let divScreen = document.querySelector("div#screen");

    //verifying
    let charClass = character.class
    if (charClass === undefined){
        let div = getDiv("Alert")
        singleSimpleMessage(div, "You must choose a class first")
        var sButton = document.querySelector("button#chooseClass")
        sButton.setAttribute("class", "doHighlight")
        return
    }

    //Setting Screen information
    console.log("Setting Thing Up")
    let gameScreen = document.querySelector("div#screen")
    gameScreen.setAttribute("class", "showdown")

    console.log(character.class)

    var ChosenEnemy = enemyRoulette()

    var enemy = {

        "icon": ChosenEnemy.icon,
        "name": ChosenEnemy.classname,
        "health": Number.parseInt(ChosenEnemy.health),
        "dmg": Number.parseInt(ChosenEnemy.damage),
        defend: function(){
            let fired = false;
            document.addEventListener("keydown",function(evt){
                if (!fired){
                   fired = true;
                   if (evt.key === "ArrowRight"){
                    document.querySelector("img#EnemyWeapon").setAttribute("class", "seen")
                    setTimeout(function(){
                        document.querySelector("img#EnemyWeapon").setAttribute("class", "enemyDefends")}, 1)
 
                    }
                }
            }, false);
        }
    }

    window.enemy = enemy

    var player = {

        "icon": character.class.src,
        "name": character.nickname,
        "health": Number.parseInt(character.class.health),
        "dmg": Number.parseInt(character.class.damage),
        atkFront: function(){
            let fired = false;
            document.addEventListener("keydown",function(evt){
                if (!fired){
                   fired = true;
                   if (evt.key === "ArrowRight"){
                    document.querySelector("img#PlayerWeapon").setAttribute("class", "seen")
                    setTimeout(function(){
                        document.querySelector("img#PlayerWeapon").setAttribute("class", "atkFront")}, 1)
                    
                    enemy.health -= player.dmg

                    console.log(`${player.name} attacked from the Front. enemies life at ${Number.parseInt(enemy.health)}`)
           } 
                }
            }, false)},
        damageBuff: async function(){
            document.addEventListener("keydown",function(evt){
                if (evt.key === "shift" && player.damageBuffUsages > 0 ){
                    document.querySelector("p#player").setAttribute("class", "dmgUP")
                    player.dmg += 20
                    player.damageBuffUsages -= 1
                    console.log("Dmg +Up", `Usages: ${player.damageBuffUsages}`)
                }
            }, false)
        },
        "damageBuffUsages": 3

    }

    let enDiv = getDiv("enemies-icon", ".classic")
    let enemyIcon = document.createElement("img");
    enemyIcon.setAttribute("src", enemy.icon)
    enemyIcon.setAttribute("alt", `Enemies-${ChosenEnemy.weapon}`)
    enemyIcon.setAttribute("id","EnemyWeapon")
    divScreen.insertBefore(enDiv.appendChild(enemyIcon), divScreen.firstChild)

    let plDiv = getDiv("player-icon",".classic")
    let playerIcon = document.createElement("img");
    playerIcon.setAttribute("src", player.icon)
    playerIcon.setAttribute("alt", `Players-${character.class.weapon}`)
    playerIcon.setAttribute("id", "PlayerWeapon")
    divScreen.insertBefore(plDiv.appendChild(playerIcon), divScreen.firstChild)

    //Battle Begin
    console.log("Starting Battle")
    
    while (true){

        player.atkFront()
        enemy.defend()
         //End of the Round interval
        await sleep(2500)

         //End Verification
         if (player.health <= 0 || enemy.health <= 0){
            if (player.health <= 0){
                let loseMessage = document.querySelector("p#lost")
                loseMessage.setAttribute("class", "seen")
                return
            } else if (enemy.health <= 0){
                let wonMessage = document.querySelector("p#won")
                wonMessage.setAttribute("class", "seen")
                return
            }
        }
        

    }
}
