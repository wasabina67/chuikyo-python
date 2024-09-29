#!/bin/bash

NUM=`cat num.txt`
MESSAGE="${NUM} の資料が公開されました。https://www.mhlw.go.jp/stf/shingi/shingi-chuo_128154.html"
URL="https://notify-api.line.me/api/notify"

curl -X POST \
    -H "Authorization: Bearer ${ACCESS_TOKEN}" \
    -F "message=${MESSAGE}" \
    ${URL}
