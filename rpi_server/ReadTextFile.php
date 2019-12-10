<?php   

    $fileObj = new fileObj('./data.txt','r');
    $fileObj -> setCsvControl(";");
    $fileObj -> setFlags(fileObj::READ_CSV);

    $JSONArray = array();

    while(!$fileObj ->eof()){
        $row = $fileObj -> current();

        $JSONArray[] = array("date"=>$row[0],"time"=>$row[1],"num"=>$row[2]);
        $fileObj -> next();
    }
    echo json_encode($JSONArray);
?>