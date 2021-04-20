awk 'BEGIN {max=0;}
{
	if(length($0)>max){
		max = length($0);
		line = $0;
	}
}END{
	print line;
}
'