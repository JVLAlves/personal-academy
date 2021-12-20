import {katana, axe, spear} from './weapon.js'
import {classes} from "./classes.js"

export var troops = { "enemies": [

    {
        "classname": "Samurai",
        "weapon": katana["weapon_name"],
        "damage": katana["damage"],
        "health": 125
    },

    {
        "classname": "Dwarf", 
        "weapon": axe["weapon_name"],
        "damage": axe["damage"], 
        "health":200
    },
    {
        "classname": "Lancer",
        "weapon": spear["weapon_name"],
        "damage": spear["damage"], 
         "health":100
    }
]
};

export function Player(nickname, Class){
    this.nickname = nickname;
    this.Class = Class
}

export function enemyRoulette(){
    let rand = Math.floor(Math.random() * (troops.enemies.length))
    console.log("Number: " + rand)
    let chosenEnemy = troops.enemies[rand]
    console.log(chosenEnemy)
    return chosenEnemy

}

