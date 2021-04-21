read c
awk 'BEGIN {FS="|";OFS="|";print "Book Name|Price|Offer"}
{
    if($3>750){
        offer = "Buy1Get2"
        print $2,$3,offer
    }
    if($3<=750 && $3>500){
        offer = "100RsCashback"
        print $2,$3,offer
    }
    if($3<500){
        offer = "FreeDelivery"
        print $2,$3,offer
    }
}
'
