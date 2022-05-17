<?php
require_once "pessoa.php";
require_once "Publicacao.php";
class livro implements Publicacao
{
    private $titulo;
    private $autor;
    private $totPaginas;
    private $pagAtual;
    private $aberto;
    private $leitor;
    private $lido;
    private $paginasLidas;

    /**
     * @param $titulo
     * @param $autor
     * @param $totPaginas
     */
    public function __construct($titulo, $autor, $totPaginas)
    {
        $this->titulo = $titulo;
        $this->autor = $autor;
        $this->totPaginas = $totPaginas;
        $this->aberto = false;
        $this->lido = false;
        $this->PagAtual = 0;
        $this->PaginasLidas = 0;

    }

    public function detalhes()
    {
        echo "<p>----------------------------------------------<br>----------------------------------------------</p>";
        echo "<p>Titulo: ".$this->getTitulo()."</p>";
        echo "<p>Autor: ".$this->getAutor()."</p>";
        echo "<p>Total de Páginas: ".$this->getTotPaginas()."</p>";
        echo "<p>Pagina lidas: ".$this->getPaginasLidas()."</p>";
        echo "<p>Pagina Atual: ".$this->getPagAtual()."</p>";
        echo "<p>Este livro já foi lido? ".($this->getLido()?"SIM":"NÃO")."</p>";
        echo "<p>Está aberto? ".($this->getAberto()?"SIM":"NÃO")."</p>";
        echo "<br><p>leitor atual: ".(isset($this->leitor)?$this->leitor->getNome():"Ninguém")."</p>";

    }

    private function aumentarVel()
    {
        if ($this->leitor->getIdade() <= 6) {
            $this->leitor->setVelLeitura($this->leitor->getVelLeitura() + 0.25);

        } elseif ($this->leitor->getIdade() > 7 && $this->leitor->getIdade() <= 12) {
            $this->leitor->setVelLeitura($this->leitor->getVelLeitura() + 0.5);

        } elseif ($this->leitor->getIdade() > 13 && $this->leitor->getIdade() <= 59) {
            $this->leitor->setVelLeitura($this->leitor->getVelLeitura() + 1);
        }
    }

    public function abrir($leitor)
    {
       if(!$this->getAberto()){
           $this->setAberto(true);
           $this->setLeitor($leitor);
       }
    }



    public function fechar()
    {
        if($this->getAberto()){
            $this->setAberto(false);
            $this->setLeitor(null);
        }
    }

    public function folhear()
    {
        if(!$this->getLido() && $this->getAberto()) {
            $maxPags = (($this->getTotPaginas() - $this->getPaginasLidas()) > $this->leitor->getVelLeitura()?$this->leitor->getVelLeitura():($this->getTotPaginas() - $this->getPaginasLidas()));
            $pags = rand(1, $maxPags);
            $this->setPagAtual($this->getPagAtual() + $pags);
            $this->setPaginasLidas($this->getPaginasLidas() + $pags);
        }
        if ($this->getPagAtual() === $this->getTotPaginas()){
            $this->setLido(true);
            $this->aumentarVel();
        }

    }

    public function avancarPag()
    {
        if(!$this->getLido() && $this->getAberto()) {
            $this->setPagAtual($this->getPagAtual() + 1);
            if ($this->getPagAtual() === $this->getTotPaginas()){
                $this->setLido(true);
                $this->aumentarVel();
            }
        }
    }

    public function voltarPag()
    {
        if(!$this->getLido()) {
            $this->setPagAtual($this->getPagAtual() -1);
        }
    }

    /**
     * @return mixed
     */
    public function getTitulo()
    {
        return $this->titulo;
    }

    /**
     * @param mixed $titulo
     */
    public function setTitulo($titulo)
    {
        $this->titulo = $titulo;
    }

    /**
     * @return mixed
     */
    public function getAutor()
    {
        return $this->autor;
    }

    /**
     * @param mixed $autor
     */
    public function setAutor($autor)
    {
        $this->autor = $autor;
    }

    /**
     * @return mixed
     */
    public function getTotPaginas()
    {
        return $this->totPaginas;
    }

    /**
     * @param mixed $totPaginas
     */
    public function setTotPaginas($totPaginas)
    {
        $this->totPaginas = $totPaginas;
    }

    /**
     * @return mixed
     */
    public function getPagAtual()
    {
        return $this->pagAtual;
    }

    /**
     * @param mixed $pagAtual
     */
    public function setPagAtual($pagAtual)
    {
        $this->pagAtual = $pagAtual;
    }

    /**
     * @return mixed
     */
    public function getAberto()
    {
        return $this->aberto;
    }

    /**
     * @param mixed $aberto
     */
    public function setAberto($aberto)
    {
        $this->aberto = $aberto;
    }

    /**
     * @return mixed
     */
    public function getLeitor()
    {
        return $this->leitor;
    }

    /**
     * @param mixed $leitor
     */
    public function setLeitor($leitor)
    {
        $this->leitor = $leitor;
    }

    /**
     * @return mixed
     */
    public function getLido()
    {
        return $this->lido;
    }

    /**
     * @param mixed $lido
     */
    public function setLido($lido)
    {
        $this->lido = $lido;
    }

    /**
     * @return mixed
     */
    public function getPaginasLidas()
    {
        return $this->paginasLidas;
    }

    /**
     * @param mixed $paginasLidas
     */
    public function setPaginasLidas($paginasLidas)
    {
        $this->paginasLidas = $paginasLidas;
    }


}
