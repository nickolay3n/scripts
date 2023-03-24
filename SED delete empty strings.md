#убираем пустые строки
sed '/^[[:space:]]*$/d' 

#Убираем каоментарии но не /#! (shell scripts)

sed -i -e '/^\s*#\([^!]\|$\)/d'

Where:

^ start of line
\s* zero or more whitespace characters
# one hash mark
\([^!]\|$\) followed by a character which is not ! or end of line.
