awk 'BEGIN{FS=";";IGNORECASE=1;}
{
    print $0;
    if($3 ~ /him/ || $2 ~ /him/ ){
        print "--> To be removed !";
        count = count+1;
    }
}END{
    if(count == "0"){print $0;}
}
'