while true
do
    THEFILE=$(inotifywait --format '%f' -qe close_write "$PWD")
    if printf '%s\n' "$(ls $PWD/*.py | xargs)" | grep -w  "$THEFILE" > /dev/null
    then
        python -m unittest 
    fi
done
