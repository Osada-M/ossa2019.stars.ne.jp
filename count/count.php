<?php

function set_count($file_name){
	$handle = fopen($file_name, 'r');
	$count = (int)fread($handle, 20) + 1;
	$handle = fopen($file_name, 'w');
	fwrite($handle, $count);
	fclose($handle);
	return $count;
}

function file_append($path, $data){
    if (!$fp = fopen($path, 'ab')) {return false;}
    flock($fp, LOCK_EX);
    $result = fwrite($fp, $data);
    fflush($fp);
    flock($fp, LOCK_UN);
    fclose($fp);
    return $result;
}

$a = set_count('countBuffer.txt');
// $f = 'count.txt';
// file_append($f, "\n");
// file_append($f, $a);
// file_append($f, "\t");
// file_append($f, $_SERVER['REMOTE_ADDR']);

?>