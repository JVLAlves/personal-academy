<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>livraria.php - 23/03/2022</title>
</head>
<body>
<?php
    require_once "livro.php";
    require_once "pessoa.php";
    $p1 = new Pessoa("João", 19, "M");
    echo"<p>O sujeito ".$p1->getNome()." é capaz de ler ".$p1->getVelLeitura()." Páginas por minuto.</p>";
    $l1 = new livro("Moby Dick", "Herman Melville", 656);
    $l1->detalhes();
    $l1->abrir($p1);
    for ($i = 0; $i<300; $i++){
        $l1->folhear();
    }
    $l1->detalhes();
?>
</body>
</html>
