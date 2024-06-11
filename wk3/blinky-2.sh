#!/usr/bin/env dash

for file in *.html
do
	if grep -q -E '<blink>' "$file"
	then
		mv "$file" "$(echo "$file" | sed -E -e 's/.html/.bad/')"
	fi
done
