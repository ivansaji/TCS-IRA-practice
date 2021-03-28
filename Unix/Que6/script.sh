awk 'BEGIN {FS=";";IGNORECASE=1;}
{
    if($3=="unpaid"){
        ar[$1]+=1;
        c=c+1;
    }
}END{
    if(c==0){
        print " ";
    }
    else{
        for(i in ar){
            if(ar[i]==1){
                print i;
            }
        }
    }
}
'$1 |sort -k1