<?php

// Create DOM from URL or file
$html = file_get_html("http://ossa2019.stars.ne.jp/index.html");

// Find all images
foreach($html->find("counter") as $element)
echo $element->src . "<br>";

?>