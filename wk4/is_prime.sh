#!/usr/bin/env dash

num="$1"

if [ "$num" -lt 2 ]
then
	echo "$num is not prime"
	exit 1
fi

testing=2
while [ "$testing" -lt "$num" ]
do
	if [ "$(( $num % $testing ))" -eq 0 ]
	then
		echo "$num is not prime"
		exit 1
	fi
	testing=$(( $testing + 1 ))
done

echo "$num is prime"
