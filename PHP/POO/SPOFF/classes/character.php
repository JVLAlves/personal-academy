<?php

abstract class character
{
    private $name;
    private $life;
    private $strength;

    public abstract function attack($who);
    public abstract function defend();

    /**
     * @return mixed
     */
    public function getName()
    {
        return $this->name;
    }

    /**
     * @param mixed $name
     */
    public function setName($name)
    {
        $this->name = $name;
    }

    /**
     * @return mixed
     */
    public function getLife()
    {
        return $this->life;
    }

    /**
     * @param mixed $life
     */
    public function setLife($life)
    {
        $this->life = $life;
    }

    /**
     * @return mixed
     */
    public function getStrength()
    {
        return $this->strength;
    }

    /**
     * @param mixed $strength
     */
    public function setStrength($strength)
    {
        $this->strength = $strength;
    }


}
