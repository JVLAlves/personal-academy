<?php
require_once "pessoa.php";
class aluno extends Pessoa
{
    private $mat;
    private $curso;

    public function cancelarMatr() {
        echo "<p>Mátricula será cancelada.</p>";
    }

    /**
     * @return mixed
     */
    public function getMat()
    {
        return $this->mat;
    }

    /**
     * @param mixed $mat
     */
    public function setMat($mat)
    {
        $this->mat = $mat;
    }

    /**
     * @return mixed
     */
    public function getCurso()
    {
        return $this->curso;
    }

    /**
     * @param mixed $curso
     */
    public function setCurso($curso)
    {
        $this->curso = $curso;
    }


}
