#!/usr/bin/env dash

# Within functions, arguments passed to the script aren't accessible, so you
# need to either save them to variables, or pass them as arguments to the
# function.
arg1=$1

progname=$(basename "$0")

help() {
	echo "Error: $@"
	echo
	echo "Usage: $progname FILE..."
	echo "Supported filetypes: zip tar.xz tar.gz"
}

if [ "$#" -eq 0 ]; then
	# Use help "$1" to pass arguments to the script to the function
	help "No file specified"
fi

for archive in "$@"
do
	case "$archive" in
		*.zip)
			unzip "$archive"
			;;
		*.tar.xz | *.tar.gz)
			tar xvf "$archive"
			;;
		*)
			help "Don't know how to extract $archive"
			;;
	esac
done
