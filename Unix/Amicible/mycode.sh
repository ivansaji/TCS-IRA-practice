awk 'BEGIN {
    read a;
    read b;
}
END{
    find_amicable(a,b);
}

function find_amicable(a,b){
    sum_a=find_divisors(a);
    sum_b=find_divisors(b);
    
    if(sum_a==b && sum_b==a)
    {
        print "The pair is amicable";
    }
    else
    {
        print "The pair is not amicable";
    }
    
}

function find_divisors(n){
    sum = 0;
    for(i=1;i<n;i++)
    {
        if(n1%i==0)
        s1=s1+i;
    }
    return sum;
}
'