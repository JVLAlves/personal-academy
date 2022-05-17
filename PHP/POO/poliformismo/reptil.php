<?php
require_once "animals.php";
class reptil extends animal
{
    private $corEscama;

    public function locomover()
    {
        echo "<p>Rastejando</p>";
    }

    public function alimentar()
    {
        echo "<p>Comendo vegetais.</p>";
    }

    public function emitirSom()
    {
        echo "<p>Sons de Réptil</p>";
    }

    /**
     * @return mixed
     */
    public function getCorEscama()
    {
        return $this->corEscama;
    }

    /**
     * @param mixed $corEscama
     */
    public function setCorEscama($corEscama)
    {
        $this->corEscama = $corEscama;
    }


}
