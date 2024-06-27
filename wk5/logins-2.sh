#!/usr/bin/env dash

z1=0
z2=0
z3=0
z4=0
z5=0
z6=0
z7=0
z8=0
z9=0
z0=0

while read zid pty from rest
do
	case "$zid" in
		z1*) z1=$(($z1 + 1)) ;;
		z2*) z2=$(($z2 + 1)) ;;
		z3*) z3=$(($z3 + 1)) ;;
		z4*) z4=$(($z4 + 1)) ;;
		z5*) z5=$(($z5 + 1)) ;;
		z6*) z6=$(($z6 + 1)) ;;
		z7*) z7=$(($z7 + 1)) ;;
		z8*) z8=$(($z8 + 1)) ;;
		z9*) z9=$(($z9 + 1)) ;;
		z0*) z0=$(($z0 + 1)) ;;
	esac
done

echo "z1=$z1"
echo "z2=$z2"
echo "z3=$z3"
echo "z4=$z4"
echo "z5=$z5"
echo "z6=$z6"
echo "z7=$z7"
echo "z8=$z8"
echo "z9=$z9"
echo "z0=$z0"
