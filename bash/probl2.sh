#!/bin/bash

filename="epa-http.txt"
arr_sites=
arr_visits=
redo_min=true #just for optimization
regex="(.+) \[.+\] \".+\" [0-9]+ ([0-9]+|-)"
min_index=0
while read line
do
    [[ $line =~ $regex ]]
    site="${BASH_REMATCH[1]}"
    visits="${BASH_REMATCH[2]}"
    if [ "${visits}" == "-" ]; then
        visits="0"
    fi
    new_element="[${visits}] ${site}"

    arr_visits_length=${#arr_sites[@]}

    if [[ "${arr_visits_length}" -lt 10 ]]; then
        arr_sites+=("${site}")
        arr_visits+=("${visits}")
    else
        if [[ "$redo_min" = true ]]; then
            for (( i=0; i<arr_visits_length; i++ ))
            do
                if [[ "${arr_visits[$i]}" -lt "${arr_visits[$min_index]}" ]]; then
                    min_index=$i
                fi
            done
        fi
        if [[ "${visits}" -gt "${arr_visits[$min_index]}" ]]; then
            arr_visits[$min_index]=$visits
            arr_sites[$min_index]=$site
            redo_min=true
        fi
    fi
done < "$filename"
for (( i=0; i<arr_visits_length; i++ ))
do
    echo "${arr_sites[$i]}: ${arr_visits[$i]}"
done
