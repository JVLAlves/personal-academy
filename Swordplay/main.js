import {troops} from "./objects.js"
import {character} from "./menuactions.js"

var startButton = document.querySelector("button#starting")
startButton.addEventListener("click", battle, false)

export async function battle(){
    //Setting entities information
    console.log("Setting Thing Up")
    let gameScreen = document.querySelector("div#screen")
    gameScreen.setAttribute("class", "seen")
    var PlayerName = character.nickname
    var playerLife = Number.parseInt(character.class.health)
    var playerDmg = Number.parseInt(character.class.damage)

    let plyrHp = document.querySelector("p#player")
    let enemHp = document.querySelector('p#enemy')

    var enemyName = troops.enemies[0].classname
    var enemyLife = Number.parseInt(troops.enemies[0].health)
    var enemyDmg = Number.parseInt(troops.enemies[0].damage)

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
            let playerTextContent = `Player: ${playerLife}`
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

function sleep(milliseconds) {  
    return new Promise(resolve => setTimeout(resolve, milliseconds));  
 } 


