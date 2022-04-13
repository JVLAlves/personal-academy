<?php

abstract class animal
{

    protected $peso;
    protected $idade;
    protected $membros;
    public abstract function locomover();
    public abstract function alimentar();
    public abstract function emitirSom();

}
