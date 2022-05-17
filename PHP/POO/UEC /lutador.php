<?php

class Lutador
{
private $nome;
private $nacionalidade;
private $idade;
private $altura;
private $peso;
private $categoria;
private $vitorias;
private $derrotas;
private $empates;


    /**
     * @param $nome
     * @param $nacionalidade
     * @param $idade
     * @param $altura
     * @param $peso
     * @param $categoria
     * @param $vitorias
     * @param $derrotas
     * @param $empates
     */
    public function __construct($nome, $nacionalidade, $idade, $altura, $peso, $vitorias, $derrotas, $empates)
    {
        $this->setNome($nome);
        $this->setNacionalidade($nacionalidade);
        $this->setIdade($idade);
        $this->setAltura($altura);
        $this->setPeso($peso);
        $this->setVitorias($vitorias);
        $this->setDerrotas($derrotas);
        $this->setEmpates($empates);
       ;
    }

    public function apresentar(){
    echo "<p>----------------------------------------------<br>----------------------------------------------</p>";

    echo    "<p> Lutador:  <strong class='name'>".$this->getNome()."</strong></p>";
    echo    "<p>Origem: ".$this->getNacionalidade()."</p>";
    echo    "<p>Idade: ".$this->getIdade()." anos</p>";
    echo    "<p>Altura: ".$this->getAltura()."m</p>";
        echo    "<p>Peso: ".$this->getPeso()."Kg</p>";
    echo    "<p>Categoria: Peso ".$this->getCategoria()."</p>";
}
public function status()
{
    echo "<p>----------------------------------------------</p>";
    echo "<p>Vitórias: ".$this->getVitorias()."</p>";
    echo "<p>Derrotas: ".$this->getDerrotas()."</p>";
    echo "<p>Empates: ".$this->getEmpates()."</p>";
}
public function ganharLuta()
{
    $this->setVitorias($this->getVitorias()+1);
}
public function perderLuta()
{
    $this->setDerrotas($this->getDerrotas()+1);
}
public function empatarLuta()
{
$this->setEmpates($this->getEmpates()+1);
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
    public function getNacionalidade()
    {
        return $this->nacionalidade;
    }

    /**
     * @param mixed $nacionalidade
     */
    public function setNacionalidade($nacionalidade)
    {
        $this->nacionalidade = $nacionalidade;
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
    public function getAltura()
    {
        return $this->altura;
    }

    /**
     * @param mixed $altura
     */
    public function setAltura($altura)
    {
        $this->altura = $altura;
    }

    /**
     * @return mixed
     */
    public function getPeso()
    {
        return $this->peso;
    }

    /**
     * @param mixed $peso
     */
    public function setPeso($peso)
    {
        $this->peso = $peso;
        $this->setCategoria();
    }


    /**
     * @return mixed
     */
    public function getCategoria()
    {
        return $this->categoria;
    }

    /**
     * @param mixed $categoria
     */
    private function setCategoria()
    {
        if ($this->getPeso() < 52.2){
            $this->categoria = "Inválido";
        } elseif ($this->getpeso() <= 70.3){
            $this->categoria = "Leve";
        } elseif ($this->getPeso() <= 83.9){
            $this->categoria = "Médio";
        } elseif ($this->getPeso()){
            $this->categoria = "Pesado";
        } else {
            $this->categoria = "Inválido";
        }

    }

    /**
     * @return mixed
     */
    public function getVitorias()
    {
        return $this->vitorias;
    }

    /**
     * @param mixed $vitorias
     */
    public function setVitorias($vitorias)
    {
        $this->vitorias = $vitorias;
    }

    /**
     * @return mixed
     */
    public function getDerrotas()
    {
        return $this->derrotas;
    }

    /**
     * @param mixed $derrotas
     */
    public function setDerrotas($derrotas)
    {
        $this->derrotas = $derrotas;
    }

    /**
     * @return mixed
     */
    public function getEmpates()
    {
        return $this->empates;
    }

    /**
     * @param mixed $empates
     */
    public function setEmpates($empates)
    {
        $this->empates = $empates;
    }



}
