<?php
require_once 'character.php';
class dwarf extends character
{
    public function __construct($name)
    {
        $this->setName($name);
        $this->setHealth(200);
        $this->setWeapon("<img src='images/waraxe.svg' alt='war-axe'/>");
    }
}
