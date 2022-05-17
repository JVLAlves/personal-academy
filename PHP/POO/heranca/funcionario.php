<?php

class funcionario extends pessoa
{
    private $setor;
    private $trabalhando;
    public function mudarTrabalho(){
        $this->trabalhando = ! $this->trabalhando;
    }

    /**
     * @return mixed
     */
    public function getSetor()
    {
        return $this->setor;
    }

    /**
     * @param mixed $setor
     */
    public function setSetor($setor)
    {
        $this->setor = $setor;
    }

    /**
     * @return mixed
     */
    public function getTrabalhando()
    {
        return $this->trabalhando;
    }

    /**
     * @param mixed $trabalhando
     */
    public function setTrabalhando($trabalhando)
    {
        $this->trabalhando = $trabalhando;
    }

}
