read c
awk 'BEGIN {FS=","}
{
	if($3>max)
	{
		max=$3;
		name=$2;
		id=$1;

		print max,name,id
	}
}
'