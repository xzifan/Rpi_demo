<?php


    $str = $_GET["str"];

    $data = http_build_query(array(
        'str' => $str
    ));

    // Create HTTP stream context
    $context = stream_context_create(array(
        'http' => array(
            'method' => 'GET',
        )
    ));

    // Make GET request
    $response = file_get_contents("http://users.du.se/~h19zifxi/ik2018distr/server_write_temp.php?str=$str", false, $context);

?>