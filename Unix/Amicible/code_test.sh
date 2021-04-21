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
function findDivisors(n)
{
    sum = 1
    sqrtNo = sqrt(n)
    for (i = 2; i <= sqrtNo; i++)
        if (n % i == 0 )
            if (i == n % i)
                sum += i
            else
                sum += i+n/i
    return sum
}'
