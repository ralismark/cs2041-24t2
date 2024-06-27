#!/usr/bin/env dash

count=0

while read line
do
	case "$line" in
		*uniwide-pat-pool*)
			count=$(($count + 1))
			;;
	esac
done

echo "$count"
