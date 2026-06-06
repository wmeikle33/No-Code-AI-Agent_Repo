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
