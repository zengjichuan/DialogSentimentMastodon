#/bin/bash

inst="https://mastodon.macsnet.cz/api/v1/timelines/public?local=1"

touch toots.txt
while true; do
    curl "$inst" >> toots.txt
    nexturl=$(curl -I "$inst" | grep -e '^Link:' tt | cut -d' ' -f2 | sed 's,<,,g;s,>,,;s,;,,')
    echo nexturl" $nexturl"
    if [ "$nexturl" == "" ]; then
      break
    fi
    inst="$nexturl"
    sleep 1
    break
done

