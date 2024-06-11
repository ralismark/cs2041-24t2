#!/usr/bin/env dash

while read zid mark
do
	if echo "$mark" | grep -E -q "^[0-9]+$"
	then
		echo "$zid $(($mark + 1))"
	else
		echo "$mark is not a number"
	fi
done
