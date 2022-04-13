<?php
require_once "animals.php";
class peixe extends animal
{
    private $corEscama;

    public function locomover()
    {
        echo "<p>Nadando</p>";
    }

    public function alimentar()
    {
        echo "<p>Comendo Substâncias</p>";
    }

    public function emitirSom()
    {
        echo "<p>Peixes não emitem som.</p>";
    }

    public function soltarBolha(){
        echo "<p>Soltando Bolha!</p>";
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
