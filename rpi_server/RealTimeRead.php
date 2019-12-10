<?php
    header('content-Type:text/event-stream');
    header('Cache-Control:no-cache');

    $file = new SplFileObject("./data.txt","r");
    $str = "";

        $file->seek($file->getSize());
        $linesTot = $file->key();

        $file->seek($linesTol-1);
        echo "data:" . $file->current() . "\n\n";
    
    flush()

?>