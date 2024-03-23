<?php

function set_count($file_name){
	$handle = fopen($file_name, 'r');
	$count = (int)fread($handle, 20);
	fclose($handle);
	return $count;
}
$a = set_count("count.txt");

require_once 'simple_html_dom.php';
$dom = file_get_html("../index.html");
$dom->find('counter',0)->outertext = $a;
echo $a;

$body = $dom->save();
$dom->clear();

echo $body;

?>