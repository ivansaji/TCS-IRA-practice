tr "/" ";" | tr "-" ";"| awk 'BEGIN {FS=";"; IGNORECASE=1;}
{
	if($2=="08" || $2=="Aug"){
		bonus = bonus + 0.1*$5;
		c=c+1;
	}
}END{
	if(c>0){
		print bonus;
	}
	else{
		print 0;
	}
}
'