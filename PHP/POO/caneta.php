<?php

class caneta
{
private $modelo;
private $cor;
private $ponta;
private $tampada;

    /**
     * @param $modelo
     * @param $cor
     * @param $ponta
     */
    public function __construct($modelo, $cor, $ponta)
    {
        $this->modelo = $modelo;
        $this->cor = $cor;
        $this->ponta = $ponta;
    }


    /**
     * @return mixed
     */
    public function getModelo()
    {
        return $this->modelo;
    }

    /**
     * @param mixed $modelo
     */
    public function setModelo($modelo)
    {
        $this->modelo = $modelo;
    }

    /**
     * @return mixed
     */
    public function getCor()
    {
        return $this->cor;
    }

    /**
     * @param mixed $cor
     */
    public function setCor($cor)
    {
        $this->cor = $cor;
    }

    /**
     * @return mixed
     */
    public function getTampada()
    {
        return $this->tampada;
    }

    /**
     * @param mixed $tampada
     */
    public function setTampada($tampada)
    {
        $this->tampada = $tampada;
    }

    /**
     * @return mixed
     */
    public function getPonta()
    {
        return $this->ponta;
    }

    /**
     * @param mixed $ponta
     */
    public function setPonta($ponta)
    {
        $this->ponta = $ponta;
    }

}
