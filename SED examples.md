# убираем пустые строки
`sed '/^[[:space:]]*$/d'` 

# Убираем каоментарии но не #! (shell scripts)

`sed -i -e '/^\s*#\([^!]\|$\)/d'`

Where:

`^` start of line
`\s*` zero or more whitespace characters
#one hash mark
`\([^!]\|$\) followed by a character which is not ! or end of line.`

# замена куча всякой дряни
`sed -n "\
s|IPAddress=not assigned;||p; \
s|Server-Name=|hostname;|p; \
s|^Name=|Name;|p; \
s|IPAddress=|IP;|p; \
s|Total=|TotalMemory;|p; \
s|Free=|FreeMemory;|p; \
s|Used=|UsedMemory;|p; \
s|ReadSpeed=|ReadSpeed;|p; \
s|TransmitSpeed=|TransmitSpeed;|p; \
s|AdapterStatus=|AdapterStatus;|p; \
s|CPU1 Status=|CPU1Status;|p; \
s|CPU2 Status=|CPU2Status;|p; \
s|DISK[.+]=|DISK[.+];|p \
"`
# подстановка глобальных переменных (например из докера)
`sed -i '-s|%OWNER%|'"$OWNER"'|g' /vaw/www/html/index.html`

`cat index.html`

`<html><body><h1>%OWNER%</h1></body></html>`

# будет дополняться
