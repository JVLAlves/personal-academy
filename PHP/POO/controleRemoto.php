<?php
//Esse é minha classe encapsulada. Implementada pela interface Controlador.
require_once 'Controlador.php';
class controleRemoto implements Controlador
{
    private $volume;
    private $ligado;
    private $tocando;

    /**
     * @param $volume
     * @param $ligado
     * @param $tocando
     */
    public function __construct()
    {
        $this->volume = 50;
        $this->ligado = false;
        $this->tocando = false;
    }

    /**
     * @return int
     */
    private function getVolume()
    {
        return $this->volume;
    }

    /**
     * @param int $volume
     */
    private function setVolume($volume)
    {
        $this->volume = $volume;
    }

    /**
     * @return false
     */
    private function getLigado()
    {
        return $this->ligado;
    }

    /**
     * @param false $ligado
     */
    private function setLigado($ligado)
    {
        $this->ligado = $ligado;
    }

    /**
     * @return false
     */
    private function getTocando()
    {
        return $this->tocando;
    }

    /**
     * @param false $tocando
     */
    private function setTocando($tocando)
    {
        $this->tocando = $tocando;
    }


    public function ligar()
    {
        $this->setLigado(true);
    }

    public function desligar()
    {
        $this->setLigado(false);
    }

    public function abrirMenu()
    {
        echo "<br><p>A televisão está: <strong>".($this->getLigado()?"Ligada":"Desligada")."</strong></p>";
        echo"<br><p>Está tocando?: ". ($this->getTocando()?"SIM":"NÃO");
        echo "<br><p>".$this->getVolume()."% ";
        for ($i=0; $i <= $this->getVolume(); $i+=10){
            echo "|";
        }
        echo "<br>";
    }

    public function fecharMenu()
    {
        echo"<br><p>Fechando menu.</p>";
    }

    public function maisVolume()
    {
        if ($this->getLigado()){
            $this->setVolume($this->getVolume() + 5);
        }
    }

    public function menosVolume()
    {
       if ($this->getLigado() && $this->getVolume() > 0){
           $this->setVolume($this->getVolume() - 5);

       }
    }

    public function ligarMudo()
    {
       if ($this->getLigado() && $this->getVolume() > 0){
           $this->setVolume(0);
       }
    }

    public function desligarMudo()
    {
        if ($this->getLigado() && $this->getVolume() == 0){
            $this->setVolume(50);
        }
    }

    public function play()
    {
        if ($this->getLigado() && !$this->getTocando()){
            $this->setTocando(true);
        }
    }

    public function pause()
    {
        if ($this->getLigado() && $this->getTocando()){
            $this->setTocando(false);
        }
    }
}
