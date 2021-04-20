tr "-" "|" | awk 'BEGIN {FS="|"}
{
	if($3<=04){
		print $1;
	}
}
'