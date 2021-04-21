awk 'BEGIN {FS=",";IGNORECASE=1;c=0;OFS="#"}
{
	if($5 ~/yes/ && $3>=60){
		print $2,$3;
		c=c+1;
	}
}END{
	if(c>0){
		print c;
	}
	else{
		print "No records found";
	}
}
'