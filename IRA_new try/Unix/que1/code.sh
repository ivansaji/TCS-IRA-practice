awk 'BEGIN {FS=","}
{
	if($4<60){
		print $1;
	}
}'|uniq|sort