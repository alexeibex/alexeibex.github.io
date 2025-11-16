import shutil
import os

# Define the paths
source = 'assets/css/Alexei_Furs_Resume.pdf'
destination = 'assets/Alexei_Furs_Resume.pdf'

# Execute the move
if os.path.exists(source):
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    shutil.move(source, destination)
    print(f"SUCCESS: Moved {source} to {destination}")
else:
    print(f"ERROR: Source file {source} not found. Please check if it's already moved.")