<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="../style.css">
    <title>media.php - 14/03/2022</title>
</head>
<body>
<div>
    <?php
     $n1 = isset($_GET["n1"])?$_GET["n1"]:0;
     $n2 = isset($_GET["n2"])?$_GET["n2"]:0;
     $media = ($n1 + $n2)/2;
    if ($media < 5.0){
         $status = "REPROVADO";
     }
     elseif ($media >= 5.0 && $media < 7.0){
         $status = "EM RECUPERAÇÃO";
     }
     else {
         $status = "APROVADO";
     }

     echo "O aluno tirou $n1 na primeira avaliação e $n2 na segunda, logo está <span class='status'>$status</span>."

    ?>
</div>
<br>
<a href="media.html">Voltar</a>
</body>
</html>