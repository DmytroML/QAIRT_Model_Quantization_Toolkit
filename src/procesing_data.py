from ultralytics.utils.downloads import download

# This automatically downloads and extracts COCO128 into a '../datasets' folder
url = 'https://ultralytics.com/assets/coco128.zip'
download(url, dir='.')


import os
import zipfile
import urllib.request

# Define URL and filenames
url = "https://ultralytics.com/assets/coco128.zip"
zip_path = "coco128.zip"
extract_path = "./coco128_dataset"

# Download the file
print("Downloading COCO128...")
urllib.request.urlretrieve(url, zip_path)

# Extract the file
print("Extracting files...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

# Clean up zip file
os.remove(zip_path)
print(f"Done! Dataset saved to: {os.path.abspath(extract_path)}")
