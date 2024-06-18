#!/usr/bin/env dash

if [ "$#" -ne 1 ]
then
	echo "you must pass exactly one argument"
	exit
fi

acc "$1" |
sed -n -E -e '/User classes/,/Misc classes/p' |
sed -E -e '/Misc classes/d' |
cut -d: -f2- |
tr , '\n' |
sed -E -e 's/^ //' |
grep -E '[A-Z]{4}' |
grep -E 'Student' |
cut -dt -f1
