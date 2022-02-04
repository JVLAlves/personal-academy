import {katana, axe, spear, fist} from "./weapon.js";

export var classes = {

    "villager": {
    
    "src": "images/smeralderest.png",
    "classname": "Villager",
    "weapon": fist["weapon_name"],
    "damage": fist["damage"],
    "health": 100,
    },

    "samurai": {

    "src": "images/katana-100x300.png",
    "classname": "Samurai",
    "weapon": katana["weapon_name"],
    "damage": katana["damage"],
    "health": 100
    },

    "dwarf": {

    "src": "images/Axe.png",
    "classname": "Dwarf",
    "weapon": axe["weapon_name"],
    "damage": axe["damage"],
    "health": 100

    },

    "lancer": {
    "src": "images/Spear-100x400.png",
    "classname": "Lancer",
    "weapon": spear["weapon_name"],
    "damage": spear["damage"],
    "health": 100
    },
    }
