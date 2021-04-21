awk 'BEGIN {
    getline a;
    getline b;
}
END{
    print "The inputs are\n"
    print a;
    print b;
    
    print "Finding Sum of Divisors\n"
    asum=1
    bsum=1

    print "Finding sum of dev 1"
    
    for (i = 2; i < a; i++)
        if(a%i==0)
            asum=asum+i;
    
    print "Finding sum of dev 2\n"    
    
    for (i = 2; i < b; i++)
        if(b%i==0)
            bsum=bsum+i
        
    print "The sum of divisors are\n"
    print asum
    print bsum

    if((asum==b)&&(bsum==a))
        print "\nThe functionis amicable"
    
    else
        print "\nThe function is not amicable"

}
'