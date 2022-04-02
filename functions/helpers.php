<?php
    function debug_log ($data, $id, $file, $append) {
        $data = '['.$id.']#######'."\r\n".print_r($data, true)."\r\n";
        if ($append == true) {
            file_put_contents('logs/'.$file, $data, FILE_APPEND | LOCK_EX);
        } else {
            file_put_contents('logs/'.$file, $data);
        }
    }
 ?>