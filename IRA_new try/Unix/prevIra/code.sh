awk 'BEGIN {FS=",";}
{
	if(max<$3){
		max=$3;
		id=$1;
		name=$2;
	}
}END{
	print id," ",name;
}
'|sort