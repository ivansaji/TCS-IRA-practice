awk 'BEGIN {FS="|"}
{
	if($3>=45 && $3<50){
		grace=50-$3
		print S1,$2,grace
	}
}'|uniq|sort