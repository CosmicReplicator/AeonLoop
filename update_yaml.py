import os
import glob

# Path to your papers folder
papers_folder = "./Papers"
# Template for YAML front matter. You might want to change the title dynamically.
yaml_header = """---
layout: default
title: {page_title}
---
"""

# Process all HTML files in the folder (if your pages are Markdown, change "*.html" to "*.md")
files = glob.glob(os.path.join(papers_folder, "*.html"))

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if the file already has YAML front matter
    if content.startswith("---"):
        print(f"Skipping {file_path}: already has YAML front matter.")
        continue
    
    # Optionally, derive a title from the filename, e.g., remove extension and replace underscores
    base_name = os.path.basename(file_path)
    title = os.path.splitext(base_name)[0].replace("_", " ").strip()
    
    # Create the YAML header with the derived title
    header = yaml_header.format(page_title=title)
    new_content = header + "\n" + content
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Updated {file_path}")

print("Bulk update complete.")

