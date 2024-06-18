#!/usr/bin/env dash

testing=2
while [ "$testing" -lt "$1" ]
do
	if ./is_prime.sh "$testing" > /dev/null
	then
		echo "$testing"
	fi
	testing=$(( $testing + 1 ))
done
