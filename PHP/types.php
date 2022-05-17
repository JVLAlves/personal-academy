<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <title></title>
</head>
<body>
<div>
    <?php
    //Tipos e Variaveis
    $n = 4;
    $no = (string) "João";
    echo "<h1>Sobre tipos e variaveis</h1> <br><br>";
    echo $no. " tem ". $n. " anos da faculdade. <br>";
    echo "$no ainda tem $n dentes na boca.<br><br>";

    //Operadores aritméticos
    $n1 = $_GET["a"];
    $n2 = $_GET["b"];
    $s = $n1 + $n2;
    $m = $n1 * $n2;
    $sub = $n1 - $n2;
    $div = $n1 / $n2;
    $mod = $n1 % $n2;
    echo "<br><h1>Sobre Operadores</h1>";
    echo "<br><h2>Operadores aritméticos</h2>";
    echo "$n1 + $n2 = $s <br>";
    echo "$n1 - $n2 = $sub <br>";
    echo "$n1 * $n2 = $m <br>";
    echo "$n1 / $n2 = $div <br>";
    echo "$n1 % $n2 = $mod <br>";

    //Operadores de atribuição
    echo "<br><h2>Operadores de atribuição</h2>";
    $atual = 2022;
    echo "Pre-atribuição (decremento ou incremento) realiza a operação e depois apresenta a variavel. Por Exemplo:";
    echo "<br>O Ano atual é $atual e o ano anterior foi " . --$atual;
    echo "<br><br>Já a pós-atribuição (decremento ou incremento) apresenta a variavel e depois realiza a operação. Por exemplo:";
    echo "<br>" . $atual-- . " > $atual mas são a mesma variavel.";

    $x = "abc";
    $$x = "def";
    echo "<br><br>A variável x recebe $x e a variável $x criada recebe $abc.<br>";

    //Operadores Relacionais e Operador Unário.
    echo "<br><h2>Operadores Relacionais</h2>";
    echo "Os operadores relacionais sâo:<ul><li>Maior - ( > )</li><li>Menor - ( < )</li><li>Maior ou igual - (>=)</li><li>Menor ou igual - (<=)</li><li>Diferente  - (<>) ou (!=)</li><li>Igual - (==)</li><li>Idêntico - (===)</li></ul>";
    echo "<br>Já o operador <ins>Unário</ins> funciona na seguinte forma:<br><br><em>expressão</em> ? <em>verdadeiro</em> : <em>falso</em><br>";
    echo "<br>Exemplos:<br>";

    $tipo = $_GET["op"];
    echo" Os valores foram   $n1 e $n2<br>";
    $r = ($tipo == "s")?$n1 + $n2:$n1 * $n2;
    echo "O resultado será $r.<br>";

    echo "<br><h2>Operadores Lógicos</h2>";
    echo "Os operadores são:<ul><li>AND - &&</li><li>OR - ||</li><li>XOR</li><li>( ! )</li></ul>";
    echo "<br>Exemplos:<br>";
    $ano = $_GET["an"];
    $idade = 2022 - $ano;
    echo "Quem nasceu em $ano tem $idade anos. ";
    $tipo = ($idade >= 18 && $idade <65)?"OBRIGATORIO": "NAO OBRIGATORIO";
    echo "E dessa forma seu voto é $tipo."




    ?>

</div>
</body></html>

