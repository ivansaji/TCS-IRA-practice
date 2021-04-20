read c
awk 'BEGIN {FS=";"}
{
	if($4 ~/^A/ || $4 ~/^N/ || $4 ~/^H/){
		print $1
	}
}
'