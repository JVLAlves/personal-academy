<?php

class pessoa
{
    private $nome;
    private $idade;
    private $sexo;
    private $velLeitura;
    /**
     * @param $nome
     * @param $idade
     * @param $sexo
     */
    public function __construct($nome, $idade, $sexo)
    {
        $this->nome = $nome;
        $this->idade = $idade;
        $this->sexo = $sexo;
        $this->velLeitura = $this->defaultVelLeitura();

    }

    public function fazerAniver()
    {
       echo "<p>Feliz Aniversário, ".$this->nome."!</p>";
       $this->setIdade($this->getIdade() + 1);
    }

    /**
     * @return mixed
     */
    public function getNome()
    {
        return $this->nome;
    }

    /**
     * @param mixed $nome
     */
    public function setNome($nome)
    {
        $this->nome = $nome;
    }

    /**
     * @return mixed
     */
    public function getIdade()
    {
        return $this->idade;
    }

    /**
     * @param mixed $idade
     */
    public function setIdade($idade)
    {
        $this->idade = $idade;
    }

    /**
     * @return mixed
     */
    public function getSexo()
    {
        return $this->sexo;
    }

    /**
     * @param mixed $sexo
     */
    public function setSexo($sexo)
    {
        $this->sexo = $sexo;
    }

    /**
     * @return mixed
     */
    public function getVelLeitura()
    {
        return $this->velLeitura;
    }

    /**
     * @param mixed $velLeitura
     */
    public function setVelLeitura($velLeitura)
    {
        $this->velLeitura = $velLeitura;
    }

    private function defaultVelLeitura()
    {
        if($this->getIdade() > 2 && $this->getidade()<= 6){
        return 1;

    } else if($this->getIdade() > 7  && $this->getIdade() <= 12){
            return 3;

        } elseif ($this->getIdade() > 13 && $this->getIdade() <= 59) {
        return 5;
    } else {
            echo "<p>idade invalida Inválido!</p>";
            return null;
        }
        }

}
