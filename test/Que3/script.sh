tr "/" ";" | tr "-" ";" |awk 'BEGIN {FS=";"}
{
    if($2=="12" && $4=="2020"){
        sum=sum+0.1*$5+$5;
        c=c+1;
    }
}END{
    if(c>0){print sum;}
    else{print 0;}
}' | sort