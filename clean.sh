#!/bin/bash

# Define the root directory
root_dir="."

# Loop through each problem folder inside the root directory
for problem_dir in "$root_dir"/*; do
  # Check if it is a directory
  if [ -d "$problem_dir" ]; then
    echo "Processing $problem_dir"
    
    # Loop through each folder inside the problem folder
    for sub_dir in "$problem_dir"/*; do
      # Check if it is a directory and does not have the name "Accepted"
      if [ -d "$sub_dir" ] && [[ "$(basename "$sub_dir")" != "Accepted" ]]; then
        echo "Deleting $sub_dir"
        rm -rf "$sub_dir"
      fi
    done
    
    # Loop through each file inside the problem folder
    for file in "$problem_dir"/*; do
      # Check if it is a file and does not have the name "Accepted"
      if [ -f "$file" ] && [[ "$(basename "$file")" != "Accepted" ]]; then
        echo "Deleting $file"
        rm -f "$file"
      fi
    done
  fi
done

echo "Cleanup completed."

