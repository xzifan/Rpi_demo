<?php


    $str = $_GET["str"];

    // $url = 'http://users.du.se/~h19zifxi/ik2018distr/server_write_temp.php';
    // $ch = curl_init($url);

    // curl_setopt($ch, CURLOPT_POST, 1);
    // curl_setopt($ch, CURLOPT_POSTFIELDS, $str);
    // curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    // $response = curl_exec($ch);
    // curl_close($ch);
    $response = file_get_contents("http://users.du.se/~h19zifxi/ik2018distr/server_write_temp.php?str=$str")
    echo $response

?>