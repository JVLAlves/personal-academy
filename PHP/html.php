<!DOCTYPE html>
<head>
    <?php
    $txt = isset($_GET["t"])?$_GET["t"]:"Texto Genérico";
    $tam = isset($_GET["tam"])?$_GET["tam"]:"12pt";
    $cor = isset($_GET["cor"])?$_GET["cor"]:"#000000";
    ?>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>html.php - 11/03/2022</title>
    <style>
        span.texto{
            font-size: <?php echo $tam;?>;
            color: <?php echo $cor;?>;
        }
    </style>
</head>
<body>
</form>
<div>
    <?php
    echo "<span class='texto'>$txt</span>";
    ?>
</div>
<br>
<br>
<a href="index.html">Voltar</a>

</body>
</html>