<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title>index.php - 17/03/2022</title>
</head>
<body>
    <pre>
        <?php
            require_once "controleRemoto.php";

            $c = new ControleRemoto();
            $c->ligar();
            $c->abrirMenu();


        ?>
    </pre>
</body>
</html>
