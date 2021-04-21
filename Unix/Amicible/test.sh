awk 'BEGIN {sum = 0}
END{
	for(i=0;i<10;i++){
		print i;
	}
}
'