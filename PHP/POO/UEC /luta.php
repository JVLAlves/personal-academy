<?php
require_once "lutador.php";
class luta
{
//atributos
private $desafiado;
private $desafiante;
private $rounds;
private $aprovado;

//getters e setters
    /**
     * @param $desafiado
     * @param $desafiante
     */

    /**
     * @return mixed
     */
    public function getDesafiado()
    {
        return $this->desafiado;
    }

    /**
     * @param mixed $desafiado
     */
    public function setDesafiado($desafiado)
    {
        $this->desafiado = $desafiado;
    }

    /**
     * @return mixed
     */
    public function getDesafiante()
    {
        return $this->desafiante;
    }

    /**
     * @param mixed $desafiante
     */
    public function setDesafiante($desafiante)
    {
        $this->desafiante = $desafiante;
    }

    //metodos publicos
    public function marcarLuta($l1, $l2)
    {
        if (($l1->getCategoria() === $l2->getCategoria()) && ($l1 != $l2)){
            $this->aprovado = true;
            $this->desafiante = $l1;
            $this->desafiado = $l2;
        } else {
            $this->aprovado = false;
            $this->desafiante = null;
            $this->desafiado = null;
        }
    }
    public function lutar()
    {

        if ($this->aprovado) {
            $this->rounds++;
            $this->desafiado->apresentar();
            $this->desafiante->apresentar();
            $vencedor = rand(0, 2);
            switch ($vencedor) {
                case 0:
                    echo "<h3><strong>EMPATOU!!!</strong></h3>";
                    $this->desafiado->empatarLuta();
                    $this->desafiante->empatarLuta();
                    break;
                case 1:
                    echo "<h3><strong><span class='vencedor'>" . $this->desafiado->getNome() . "</span> venceu!!!</strong></h3>";
                    $this->desafiado->ganharLuta();
                    $this->desafiante->perderLuta();
                    break;
                case 2:
                    echo "<h3><strong><span class='vencedor'>" . $this->desafiante->getNome() . "</span> venceu!!!</strong></h3>";
                    $this->desafiado->perderLuta();
                    $this->desafiante->ganharLuta();
                    break;
            }
        } else {
            echo "<p>Luta não pode acontecer.</p>";
        }

    }

}
