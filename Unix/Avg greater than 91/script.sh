awk 'BEGIN {FS="|"}
{
    if($5>=90 && $6>=87){
        avg=($5+$6)/2;
        if(avg>=91){
            {print $1"|"$2"|"$3"|"$4"|"avg;}
        }
    }
}
'|sort