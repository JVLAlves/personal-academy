<?php
require_once "animals.php";
class mamifero extends animal
{

    private $corPelo;

    public function locomover()
    {
        echo "<p>Correndo.</p>";
    }

    public function alimentar()
    {
        echo "<p>Mamando</p>";
    }

    public function emitirSom()
    {
        echo "<p>Sons de Mamífero</p>";
    }

    /**
     * @return mixed
     */
    public function getCorPelo()
    {
        return $this->corPelo;
    }

    /**
     * @param mixed $corPelo
     */
    public function setCorPelo($corPelo)
    {
        $this->corPelo = $corPelo;
    }
}
