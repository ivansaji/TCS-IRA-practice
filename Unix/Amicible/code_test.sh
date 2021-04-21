awk 'BEGIN { 
getline a
getline b
      }
END   {
        findAmicableNo(a, b)
      }
function findAmicableNo(a, b)
{
    asum = findDivisors(a)
    bsum = findDivisors(b)
    
    if (( asum == b ) && ( bsum == a ))
        print "The pair is amicable"
    else
        print "The pair is not amicable"
}
function findDivisors(c){
    sum=0
    for(i=2;i<=c;i++){
        if(c%i==0){
            sum=sum+i;
        }
    }
    return sum;
}'
