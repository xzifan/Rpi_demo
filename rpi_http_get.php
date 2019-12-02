<?php
    $file = fopen("data.txt","a");
    $file2 = fopen("data2.txt","a");

    $timeStamp = $_GET["timeStamp"];

    $file -> fwrite($timeStamp,PHP_EOL);
    $file2 -> fwrite($timeStamp,PHP_EOL);

    echo $_GET["timeStamp"];

?>