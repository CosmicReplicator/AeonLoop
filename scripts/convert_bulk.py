import os
from bs4 import BeautifulSoup

# Specify your input and output directories
input_dir = r"C:\Users\Night_Refer\Desktop\AeonLoop\github\AeonLoop\Papers"
output_dir = r"C:\Users\Night_Refer\Desktop\AeonLoop\github\test"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Process each HTML file in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(".html"):
        input_path = os.path.join(input_dir, filename)
        
        # Read the file´s content
        with open(input_path, "r", encoding="utf-8") as infile:
            html_content = infile.read()
        
        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Look for the <main> tag in the HTML
        main_tag = soup.find("main")
        if main_tag is None:
            print(f"WARNING: No <main> tag found in {filename}. Skipping...")
            continue

        # Get the content inside the <main> as HTML
        main_content = main_tag.decode_contents()
        # Optionally, remove unwanted backslashes if present
        main_content = main_content.replace("\\", "")
        
        # Use the file's name (without extension) for the page title (adjust as needed)
        page_title = os.path.splitext(filename)[0].replace("_", " ")
        
        # Prepend YAML front matter to the content
        yaml_front_matter = (
            "---\n"
            f"layout: default\n"
            f"title: \"{page_title}\"\n"
            "---\n\n"
        )
        new_file_content = yaml_front_matter + main_content
        
        # Write the processed content to a new file in the output directory
        output_path = os.path.join(output_dir, filename)
        with open(output_path, "w", encoding="utf-8") as outfile:
            outfile.write(new_file_content)
        
        print(f"Processed {filename} -> {output_path}")


