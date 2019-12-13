<?php
    $file = fopen("time_temp.txt","a") or die("fopen failed");

    $str = $_GET["str"].PHP_EOL;
    echo $str;
    fwrite($file, $str) or die("FWrite fail");
    
    fclose($file)
?>