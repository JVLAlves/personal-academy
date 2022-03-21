<?php
//Minha classe que utiliza do conhecimendo de getters, setter e metodos construtores
/**
 * getters, setters e metodos construtores podem ser criados repidamente utilizando a IDE
 * basta utilizar do comando:
 * alt + insert (ins)
 **/
class ContaBanco
{
public $numConta;
protected $tipo;
private $dono;
private $saldo;
private $status;

//metodo construtor
public function __construct(){
    $this->saldo = 0;
    $this->status = false;
}

public function abrirConta($t)
{
    $this->setTipo($t);
    $this->setStatus(true);
    if ($t == "CC"){
        $this->saldo = 50;
    } else if ($t = "CP"){
        $this->saldo = 150;
    }

}
public function fecharConta()
{
    if ($this->saldo > 0) {
        echo "Conta permanece com saldo.";
    } else if ($this->saldo < 0) {
        echo "Conta em débito. Favor pagá-lo antes de fechar a conta $this->tipo.";

    } else {
        $this->setStatus(false);
    }
}

public function depositar($v)
{
    if ($this->getStatus() == true){
        $this->setSaldo($this->getSaldo() + $v);
        echo "<p>Depósito de R$ $v realizado com sucesso na conta de ".$this->getDono().".</p>";
    } else {
        echo "Impossível realizar deposito.";
    }
}
public function sacar($v)
{
    if ($this->getStatus() == true){
        if ($this->getSaldo() >= $v){
            $this->setSaldo($this->getSaldo() - $v);
            echo"<p>Saque de R$ $v autorizado na conta de ".$this->getDono().".</p>";
        } else {
            echo "Saldo insuficiente.";
        }
    } else {
        echo "Impossível realizar saque";
    }
}

public function pagarMensal()
{
    $v = 0;
    if ($this->getTipo() == "CC"){
        $v = 12;
    } else if ($this->getTipo() == "CP"){
        $v = 20;
    }

    if ($this->getStatus()==true){
        if ($this->getSaldo() > $v){
            $this->setSaldo($this->getSaldo() - $v);
        } else {
            echo "Saldo insuficiente.";
        }
} else {
        echo "Impossível pagar.";
    }
}

//getter e setters
    /**
     * @return mixed
     */
    public function getNumConta()
    {
        return $this->numConta;
    }

    /**
     * @param mixed $numConta
     */
    public function setNumConta($n)
    {
        $this->numConta = $n;
    }

    /**
     * @return mixed
     */
    public function getTipo()
    {
        return $this->tipo;
    }

    /**
     * @param mixed $tipo
     */
    public function setTipo($t)
    {
        $this->tipo = $t;
    }

    /**
     * @return mixed
     */
    public function getDono()
    {
        return $this->dono;
    }

    /**
     * @param mixed $dono
     */
    public function setDono($d)
    {
        $this->dono = $d;
    }

    /**
     * @return mixed
     */
    public function getSaldo()
    {
        return $this->saldo;
    }

    /**
     * @param mixed $saldo
     */
    public function setSaldo($saldo)
    {
        $this->saldo = $saldo;
    }

    /**
     * @return mixed
     */
    public function getStatus()
    {
        return $this->status;
    }

    /**
     * @param mixed $status
     */
    public function setStatus($status)
    {
        $this->status = $status;
    }


}
