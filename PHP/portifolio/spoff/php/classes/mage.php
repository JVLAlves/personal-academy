<?php
require_once 'character.php';
class mage extends character
{
    public function __construct($name)
    {
        $this->setName($name);
        $this->setHealth(250);
        $this->setWeapon("<img src='images/staff.svg' alt='STAFF'/>");
    }
}
