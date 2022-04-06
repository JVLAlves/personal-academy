<?php

class battleGadget
{
    private $actionPoints;
    private $durability;
    protected $DurabilityREF;
    protected $DurabilityBar;
    private $resistance;

    /**
     * @param $actionPoints
     * @param $durability
     * @param $resistance
     */
    public function __construct($actionPoints, $durability, $resistance)
    {
        $this->actionPoints = $actionPoints;
        $this->durability = $durability;
        $this->resistance = $resistance;
        $this->DurabilityREF = $durability;
    }


    public function update($hits)
    {
        if ($this->getDurability()!=0){
            $this->setDurability($this->getDurability()-($hits/$this->getResistance()));
            if ($this->getDurability() <= 0){
                $this->setDurability(0);
                $this->DurabilityBar = 0;
            } else {
                if ($this->DurabilityREF >= $this->getDurability()){
                    $this->DurabilityBar = round((1/($this->DurabilityREF/$this->getDurability()))*100, 2);
                } else {
                    echo "<p>Error in DurabilityREF value.</p>";
                }
            }


            $this->setActionPoints($this->getActionPoints()* ($this->DurabilityBar/100));
        }
    }

    /**
     * @return mixed
     */
    public function getActionPoints()
    {
        return $this->actionPoints;
    }

    /**
     * @param mixed $actionPoints
     */
    public function setActionPoints($AP)
    {
        $this->actionPoints = $AP;
    }

    /**
     * @return mixed
     */
    public function getDurability()
    {
        return $this->durability;
    }

    /**
     * @param mixed $durability
     */
    public function setDurability($dur)
    {
        $this->durability = $dur;
    }

    /**
     * @return mixed
     */
    public function getResistance()
    {
        return $this->resistance;
    }

    /**
     * @param mixed $resistence
     */
    public function setResistance($res)
    {
        $this->resistance = $res;
    }

}
