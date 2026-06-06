def upload_file(file_path: str, upload_path):
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(target_url, files=files)

def download_file(file_path: str):
    response = requests.get(file_path)
    response.raise_for_status() 
    with open(local_filename, 'wb') as f:
        f.write(response.content)

def create_folder(folder_path):
    Path(folder_path).mkdir(parents=True, exist_ok=True)

def update_file(file_path, new_content):
    try:
        # "a" opens the file in append mode (adds text to the end)
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(new_content)
        print(f"Success: Updated '{file_path}'.")
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error updating file: {e}")

def rename_file(old_path, new_name):
    try:
        old_file = Path(old_path)
        # Create a new path string replacing the file name but keeping the folder path
        new_file = old_file.with_name(new_name)
        
        # Performs the actual rename operation
        old_file.rename(new_file)
        print(f"Success: Renamed '{old_file.name}' to '{new_name}'.")
        
    except FileNotFoundError:
        print(f"Error: The file '{old_path}' was not found.")
    except FileExistsError:
        print(f"Error: A file named '{new_name}' already exists in that folder.")
    except Exception as e:
        print(f"Error renaming file: {e}")
