#!/bin/bash
#разбор логов вида
#   [Param group=GROU]
#   field_name=value;
filename='/home/user/kav-download/0000000000000092.stat-hw'
strParamGroup=""
groupArray=()
while read -r line; do
    tempStr=$line
    if [[ "${tempStr:0:7}" == "[Param " ]] && [[ -n "$strParamGroup" ]] && [[ -n "${strParamGroup}" ]]; then
        groupArray+=( "$strParamGroup" )
        strParamGroup="" 
    fi
    if [[ "$line" != "[Param " ]]; then 
        strParamGroup="$strParamGroup\n\r$line"
    fi
done < $filename

function get_field_name {   #$1 - groupname $2 - filedname
    for index in ${!groupArray[*]}; do
        if [[ "${groupArray[$index]}" == *"$1"* ]]; then #смотрим есть ли в группе параметров нужное поле
            echo -en "${groupArray[$index]}" | while read -r newline;  do
                if [[ "${newline}" == *"$2"* ]]; then #нашли строчку с нужным полем
                echo -en "`echo "${newline}" | cut -d '=' -f2`\n"
                #echo -en "hostname;`echo "${newline}" | cut -d '=' -f2`\n"
                fi
            done
        fi
    done
} 


echo "hostname;$(get_field_name "=Server" "Server-Name=" )"
echo "hostname;$(get_field_name "aram group=CPU]" "us=" )"
echo "Network-Adapter;$(get_field_name  "Network-Adapter" "IPAddress")"
cat /home/user/kav-download/0000000000000092.stat-hw | sed -n "s/IPAddress=/IP;/p";
cat /home/user/kav-download/0000000000000092.stat-hw | sed -n "s|IPAddress=|IP;|p";

# быстрый парсинг с помощью SED -n - выводит только заменяемые строки; s - substitute; p - print; несколько выражений через ;
cat /home/user/kav-download/0000000000000092.stat-hw | sed -n "\
s|Server-Name=|hostname;|p; \
s/IPAddress=/IP;/p \
";
