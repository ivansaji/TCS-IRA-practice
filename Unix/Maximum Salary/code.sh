read c
awk '{FS=","}
{
	if($3>max){
		max=$3;
		name=$2;
		id=$1;
	}
}END{
	print id,name;
}
'