<?php   

    // $fileObj = new fileObj('./data.txt','r');
    // $fileObj -> setCsvControl(";");
    // $fileObj -> setFlags(fileObj::READ_CSV);

    // $JSONArray = array();
    
    // while(!$fileObj ->eof()){
    //     $row = $fileObj -> current();

    //     $JSONArray[] = array("date"=>$row[0],"time"=>$row[1],"num"=>$row[2]);
    //     $fileObj -> next();
    // }
    // echo json_encode($JSONArray);
    $row = 0;
    $JSONArray = array();
    if (($handle = fopen("data.txt", "r")) !== FALSE) {
        while (($data = fgetcsv($handle, 1000, ";")) !== FALSE) {
            $num = count($data);
            // echo "<p> $num fields in line $row: <br /></p>\n";
            
            // for ($c=0; $c < $num; $c++) {
            //     echo $data[$c] . "<br />\n";
            //     $JSONArray[] = array("date"=>$data[$c],"time"=>$data[$c],"num"=>$data[$c]))
            // }
            $JSONArray[$row] = array("date"=>$data[0],"time"=>$data[1],"num"=>$data[2]);

            $row++;
        }
        echo json_encode($JSONArray);
  
        fclose($handle);
    }
    // $row = 1;
    // if (($handle = fopen("data.txt", "r")) !== FALSE) {
    // while (($data = fgetcsv($handle, 1000, ";")) !== FALSE) {
    //     $num = count($data);
    //     echo "<p> $num fields in line $row: <br /></p>\n";
    //     $row++;
    //     for ($c=0; $c < $num; $c++) {
    //         echo $data[$c] . "<br />\n";
    //     }
    // }
    // fclose($handle);
    // }
?>