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

export var character = {

    class: classes["villager"],
}

export function Character(nickname, Class){
    this.nickname = nickname;
    this.Class = Class
}


