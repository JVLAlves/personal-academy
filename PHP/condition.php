<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>condition.php - 14/03/2022</title>
</head>
<body>
<div>
<?php
$ano = isset($_GET["ano"])?$_GET["ano"]:1900;
$idade = date("Y") - $ano;
echo "Você nasceu em $ano e tem $idade anos. ";
if ($idade < 16 ) {
    $vota="não pode votar";
}
elseif (($idade >=16 && $idade < 18) || ($idade > 65) ){
    $vota = "pode votar, mas é opcional";
  }
else {
    $vota = "deve votar, pois é obrigatório";
  }
echo "Com essa idade você $vota.";
?>
</div>
<br>
<br>
<a href="vota.html">Voltar</a>
</body>
</html>