function pilih(){
    printf '\e[1;32m
 __  __     ______     __  __     ______   ______   ______     __   __        ______     ______     ______  
/\ \/ /    /\  == \   /\ \_\ \   /\  == \ /\__  _\ /\  __ \   /\ "-.\ \      /\  == \   /\  __ \   /\__  _\ 
\ \  _"-.  \ \  __<   \ \____ \  \ \  _-/ \/_/\ \/ \ \ \/\ \  \ \ \-.  \     \ \  __<   \ \ \/\ \  \/_/\ \/ 
 \ \_\ \_\  \ \_\ \_\  \/\_____\  \ \_\      \ \_\  \ \_____\  \ \_\\"\_\     \ \_____\  \ \_____\    \ \_\ 
  \/_/\/_/   \/_/ /_/   \/_____/   \/_/       \/_/   \/_____/   \/_/ \/_/      \/_____/   \/_____/     \/_/ 
                                                                                                            
'
    printf "\e[1;34mType \e[1;31m ctrl+d \e[1;0m or \e[1;31mexit\e[1;33m for \e[1;31mkill \e[1;32msession\e[1;0m"
    printf "\n\e[1;36m1.\e[1;31m  Create Session\n\e[1;36m2. \e[1;31m Open Session\n"
    while true
    do
        printf "\e[1;36mPILIH :\e[1;0m"
        read pi
        if [[ $pi == "1" ]] || [[ $pi == "01" ]]; then
            printf "Session Name : "
            read ses
            tmux new-session -s $ses "python3 main3.py"
        elif [[ $pi == "2" ]] || [[ $pi == "02" ]]; then
            printf "Session Name : "
            read ses
            tmux attach -t $ses
        else
        continue
        fi

    done 
}
pilih
