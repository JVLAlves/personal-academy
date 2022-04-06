<?php
require_once 'character.php';
class elf extends character
{
    public function __construct($name)
    {
        $this->setName($name);
        $this->setHealth(250);
        $this->setWeapon("<img src='images/Axe.svg' alt='Axe'/>");
    }
}
