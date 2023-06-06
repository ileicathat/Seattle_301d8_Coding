#!/bin/bash

# Check if running as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root."
    exit 1
fi

# Get the current date and time
timestamp=$(date +%Y%m%d%H%M%S)

# Define the backup directory
backup_dir="/var/log/backups"

# Create the backup directory if it doesn't exist
mkdir -p "$backup_dir"

# Set permissions for backup directory
chmod 700 "$backup_dir"

# Print file size of log files before compression
echo "File sizes before compression:"

log_files=(
    "/var/log/syslog"
    "/var/log/wtmp"
)

for file in "${log_files[@]}"; do
    if [[ -f "$file" ]]; then
        file_size=$(du -h "$file" | awk '{print $1}')
        echo "$file: $file_size"
    else
        echo "File not found: $file"
    fi
done

# Compress log files and move them to the backup directory
echo "Compressing log files..."

for file in "${log_files[@]}"; do
    if [[ -f "$file" ]]; then
        base_name=$(basename "$file")
        zip_file="$backup_dir/$base_name-$timestamp.zip"
        zip -q "$zip_file" "$file"
        echo "Compressed file: $zip_file"
    else
        echo "File not found: $file"
    fi
done

# Clear the contents of log files
echo "Clearing log files..."

for file in "${log_files[@]}"; do
    if [[ -f "$file" ]]; then
        echo -n "" > "$file"
        echo "Cleared: $file"
    else
        echo "File not found: $file"
    fi
done

# Print file size of compressed files
echo "File sizes after compression:"

for file in "$backup_dir"/*.zip; do
    if [[ -f "$file" ]]; then
        file_size=$(du -h "$file" | awk '{print $1}')
        echo "$file: $file_size"
    else
        echo "File not found: $file"
    fi
done

# Compare sizes of compressed files to original log files
echo "Comparison of file sizes:"

for file in "${log_files[@]}"; do
    if [[ -f "$file" ]]; then
        base_name=$(basename "$file")
        original_size=$(du -h "$file" | awk '{print $1}')
        zip_file="$backup_dir/$base_name-$timestamp.zip"
        compressed_size=$(du -h "$zip_file" | awk '{print $1}')
        echo "$base_name: Original size=$original_size, Compressed size=$compressed_size"
    else
        echo "File not found: $file"
    fi
done