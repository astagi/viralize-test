#!/bin/bash
#Usage ./probl1.sh 'a b d z c f'

while true; do
	arr=(`shuf -e $1`)
    for (( i=1; i<${#arr[@]}; i++ ))
    do
        if [[ "${arr[$i-1]}" > "${arr[$i]}" ]]; then
            break
        fi
    done
    if [[ i -eq ${#arr[@]} ]];then
        break
    fi
done
for i in "${arr[@]}"
do
   echo $i
done
