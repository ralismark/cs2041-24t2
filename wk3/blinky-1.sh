#!/usr/bin/env dash

for file in *.html
do
	if grep -q -E '<blink>' "$file"
	then
		mv "$file" "$file.bad"
	fi
done
