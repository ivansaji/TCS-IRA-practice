awk 'BEGIN {FS=",";}
{
	if($4<60){
		print $1"#"$2"$"$3;
	}
}' | sort