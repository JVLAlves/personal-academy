<?php
require_once "animals.php";
class ave extends animal
{
    private $corPena;

    public function locomover()
    {
        echo "<p>Som de Ave.</p>";
    }

    public function alimentar()
    {
        echo "<p>Comendo Frutas.</p>";
    }

    public function emitirSom()
    {
        echo "<p>Sons de Ave.</p>";
    }

    public function fazerNinho()
    {
        echo "<p>Construindo um Ninho.</p>";
    }

    /**
     * @return mixed
     */
    public function getCorPena()
    {
        return $this->corPena;
    }

    /**
     * @param mixed $corPena
     */
    public function setCorPena($corPena)
    {
        $this->corPena = $corPena;
    }


}
