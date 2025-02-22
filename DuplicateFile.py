import os

def remove_duplicate_files_with_suffix(directory):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith("(1).jpg"):
            os.remove(os.path.join(directory,filename))

# Example usage
directory = "C:\\Users\\vishw\\OneDrive\\Desktop\\photo"
remove_duplicate_files_with_suffix(directory)
