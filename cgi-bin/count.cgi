open(FILE,"<count.dat");
$count = <FILE>;
close(FILE);

$count++;

open(FILE,">count.dat");
print FILE $count;
close(FILE);

print "Content-type:text/html\n\n";
print $count;
