<?php

class samurai extends character
{
    private $weapon;
    private $armor;
    private $health;
    private $damage;

    public function attack($who)
    {
        $dealt = $this->getDamage();
        if ($who->armor->getActionsPoints() != 0)
        {
            $who->armor->update($dealt);
            echo "<p>$dealt of damage dealt in armor.</p>";
            $who->setLife($who->getLife()-$dealt/2);
            echo "<p>".$dealt/2 ." of damage dealt in life.</p>";
            $who->updateHealth();
            $this->weapon->update($who->armor->getActionPoitns());
            $this->updateDamage();
        } else{
            $who->setLife($who->getLife()-$this->getDamage());
        }


    }

    protected function updateHealth()
    {
        $this->setHealth($this->getLife() + $this->armor->getActionsPoints());
    }

    protected function updateDamage()
    {
        $this->setDamage($this->getStrength() + $this->weapon->getActionsPoints());
    }

    /**
     * @return mixed
     */
    public function getWeapon()
    {
        return $this->weapon;
    }

    /**
     * @param mixed $weapon
     */
    public function setWeapon($weapon)
    {
        $this->weapon = $weapon;
    }

    /**
     * @return mixed
     */
    public function getArmor()
    {
        return $this->armor;
    }

    /**
     * @param mixed $armor
     */
    public function setArmor($armor)
    {
        $this->armor = $armor;
    }

    /**
     * @return mixed
     */
    public function getHealth()
    {
        return $this->health;
    }

    /**
     * @param mixed $health
     */
    protected function setHealth($health)
    {
        $this->health = $health;
    }

    /**
     * @return mixed
     */
    public function getDamage()
    {
        return $this->damage;
    }

    /**
     * @param mixed $damage
     */
    protected function setDamage($damage)
    {
        $this->damage = $damage;
    }

    /**
     * @return mixed
     */
    public function getIsDefending()
    {
        return $this->isDefending;
    }

    /**
     * @param mixed $isDefending
     */
    public function setIsDefending($isDefending)
    {
        $this->isDefending = $isDefending;
    }




}
