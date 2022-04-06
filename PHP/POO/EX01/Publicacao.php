<?php

interface Publicacao
{
public function abrir($leitor);
public function fechar();
public function folhear();
public function avancarPag();
public function voltarPag();
}
