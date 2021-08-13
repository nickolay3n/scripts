#!/bin/bash
$site="www.avz-site.ru"
$pass="pass"
$login="login"
hostname;`echo "${newline}" `
MYIP=`ping -c1 "${site}" | sed -nE 's/^PING[^(]+\(([^)]+)\).*/\1/p'`

curl -u "$site":"$pass" \
-b "/root/exec/cookie" \
-c "/root/exec/cookie" \
-H "Connection: keep-alive" \
-H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36" \
-i -H 'Accept:application/json' \
"https://${site}" > /dev/null

curl -u "$site":"$pass" \
-b "/root/exec/cookie" \
-c "/root/exec/cookie" \
-H "Remote Address: $MYIP:443" \
-H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" \
-H "Accept-Encoding: gzip,deflate,br" \
-H "Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7" \
-H "Connection: keep-alive" \
-H "Host: ${site}" \
-H "Referer: https://${site}/products/review/avs/AVP/kav_update/all" \
-H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36" \
-o "/home/user/kav-download/kave-"`date +%Y-%m-%d`".zip" \
"https://${site}/avs_update/kav/all/kave.zip"




#удаляем недокаченные файлы
#find /root/exec/kav -size -1000M -name "*.zip" -delete
find /home/user/kav-download -size -1000M -name "*.zip" -delete
#удаляем файлы старше трех дней
#find /root/exec/kav -mtime +3 -name "*.zip" -delete
find /home/user/kav-download -mtime +3 -name "*.zip" -delete

yourdate=`date +%Y-%m-%d`
result=`find /home/user/kav-download/  -name "*$yourdate.zip" -print | wc -l`
if [[ "$result" == "0" ]]; then
	echo "wwwww"
	nohup /root/exec/kav_download.sh > /dev/null 2>&1 &
fi
#
