<?php
require_once 'character.php';
class man extends character
{
    public function __construct($name)
    {
        $this->setName($name);
        $this->setHealth(200);
        $this->setWeapon("<img src='images/Sword.svg' alt='Sword'/>");
    }
}
