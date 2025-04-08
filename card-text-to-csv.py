import os
import glob
from collections import Counter
import csv

# Set the directory where your text files are located.
input_dir = ".\\data\\"  # update this path accordingly
# Output CSV file where the processed data will be saved.
output_file = "ml_data.csv"

# Find all files that match the pattern "*_cards_texts.txt"
all_files = glob.glob(os.path.join(input_dir, "*_cards_texts.txt"))
# Data will be {color: , text:}
data = []

for file_path in all_files:
    filename = os.path.basename(file_path)
    # Extract the color from the filename (e.g., "black_cards_texts.txt" -> "black")
    color = filename.split("_")[0]
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        # Split on double newline; adjust the split if your file uses a different separator.
        cards = content.split("\n\n")
        for card in cards:
            data.append({"color":color, "text":card})
        

# Write the processed data to a CSV file.
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames=["color", "text"]
    writer = csv.DictWriter(csvfile, fieldnames=["color", "text"])    
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f"ML data saved to {output_file}")
