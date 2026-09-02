current_date=$(date)
host=$(hostname)
user=$(whoami)
disk_usage=$(df -h)

echo "Current Date: $current_date"
echo "Hostname: $host"
echo "Username: $user"
echo "Disk Usage:"
echo "$disk_usage"

echo "Running Processes:"
ps aux

read -p "Enter a directory name to create: " dirname
read -p "Enter a filename to create inside $dirname: " filename

mkdir -p "$dirname"
touch "$dirname/$filename"

ps aux > "$dirname/$filename"

echo "Directory '$dirname' and file '$filename' created."
echo "Running processes saved into '$dirname/$filename'."
