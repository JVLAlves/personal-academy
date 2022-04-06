<!DOCTYPE html>
<html lang="en">
<head>
    <?php
    $nickname = isset($_GET['nick'])?$_GET['nick']:"DUMMY";
    $classname = isset($_GET['class'])?$_GET['class']:"man";
    $char = 0
    ?>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="../html/style.css">
    <title>SPOFF</title>
</head>
<body>
<?php

require_once 'classes/mage.php';
require_once 'classes/elf.php';
require_once 'classes/man.php';
require_once 'classes/dwarf.php';

switch($classname){
    case 'man':
        $char = new man($nickname);
        break;
    case 'dwarf':
        $char = new dwarf($nickname);
        break;
    case 'elf':
        $char = new elf($nickname);
        break;
    case 'mage':
        $char = new mage($nickname);
        break;
}

?>
<div id="weapon">
    <?php
    echo $char->getWeapon();
    ?>
</div>
<a href="../html/spoff.html">Voltar</a>
</body>
</html>
