<?php
    $file = new SplFileObject("data.txt","a") or die("fopen failed");

    $timeStamp = $_GET["timeStamp"];

    $file -> fwrite($timeStamp . PHP_EOL) or die("FWrite fail");

    echo $_GET["timeStamp"];

    ?>