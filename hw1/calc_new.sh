#!/bin/bash
echo "Calc is working!"
n1=100
n2=200
function factorial {
if [ $1 -eq 1 ]
then
echo 1
else
local temp=$(( $1 - 1 ))
local result=$(factorial $temp)
echo $(( $result * $1 ))
fi
}

while :
do
count=0
echo "Бесконечный цикл! для выхода нажми ctrl+c"
read str
for i in $str
do
	array[$count]=$i
	#echo "'$i' is the substring"
	#if [ $i == '+' ];
#	then
#		echo "yes"
		#array[$count]=$i 	
#	fi
	#echo $(($i + 1))
	count=$(($count + 1))
	#echo ${count}
done
#echo ${array[0]}
#echo ${array[1]}
#echo ${array[2]}
#echo awk'{14/4}'

x=60 
y=-9
#printf "%f\n" $((10**6 * x/y))e-6

if [ ${array[1]} == '!' ];
then
	#echo "!"
	value=${array[0]}
	result=$(factorial $value)
	echo "The recursion factorial of $value is: $result"
	fact=1                    

	for((i=2;i<=$value;i++))
	{
		fact=$((fact * i)) 
	}
	#echo $fact
	echo "The loop factorial of $value is: $fact"
	
	continue
fi

t=`echo "$str" | bc -l`
#echo $t
#if [ $t -lt 1.0 ];
#then 
#	echo "sdf"
#fi

if (( $(echo "$t < 1.0" |bc -l) )) && (( $(echo "$t > 0" |bc -l) )); then
	 echo "0"$t
	 continue
fi
if (( $(echo "$t > -1.0" |bc -l) )) && (( $(echo "$t < 0" |bc -l) )); then         
	tt=`echo "-1 * $t" | bc -l`
	echo "-0"$tt
	continue
fi


echo "$str" | bc -l
#if [ ${array[1]} == '+' ];
#then
	#echo  ${array[0]}
#	itog=$((${array[0]} + ${array[2]}))
	#echo "yes"
#	echo ${array[0]} ${array[1]} ${array[2]} = $itog
#elif [ ${array[1]} == '-' ];
#then
#	itog=$((${array[0]} - ${array[2]}))
#	echo ${array[0]} ${array[1]} ${array[2]} = $itog
#elif [ ${array[1]} == 'm' ];
#then
#	itog=$((${array[0]} * ${array[2]}))
	#echo "mul"
#	echo ${array[0]} ${array[1]} ${array[2]} = $itog
#elif [ ${array[1]} == '!' ];
#then
	#echo "!"
#	value=${array[0]}
#	result=$(factorial $value)
#	echo "The factorial of $value is: $result"


#elif [ ${array[1]} == '/' ];
#then
	#itog=$((${array[0]} / ${array[2]}))
	#itog=$((expr ${array[0]} / ${array[2]}))
	#printf "%f\n" $((10**6 * ${array[0]}/${array[2]}))e-6
	#echo ${array[0]} ${array[1]} ${array[2]} =
#	x=${array[0]}
#	y=${array[2]}
#	echo "scale=4; $x / $y" | bc
	#awk "BEGIN {print ${array[1]}/${array[2]}}"
#fi

#itog=$((${array[0]}${array[1]}${array[2]}))

#echo ${array[0]} ${array[1]} ${array[2]} = $itog 

array=()
done

