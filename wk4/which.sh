#!/usr/bin/env dash

if [ "$#" -ne 1 ]
then
	echo "you must pass exactly one argument"
	exit
fi

echo "$PATH" | tr : '\n' | while read dir
do
	a=1
	if [ -x "$dir/$1" ]
	then
		ls -l "$dir/$1"
		exit 1
	fi
done

if [ "$?" = 0 ]
then
	echo "$1 not found"
fi
