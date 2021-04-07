#!/usr/bin/bash
if [[ ${#@} != 0 ]]
then
    if [[ $(curl -s "https://krypton-byte.herokuapp.com/api/v1/check-apikey?apikey=$@")  =~ "profile" ]]
    then
        if [[ $(byobu list-session ) =~ "$@:" ]]
        then
            byobu attach -t "$@"
        else
            byobu new-session -s "$@" "python3 main3.py"
        fi
    else
        printf "APIKEY TIDAK DITEMUKAN"
    fi
else
    printf "MASUKAN APIKEY"
fi
