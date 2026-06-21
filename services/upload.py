import os
from werkzeug.utils import secure_filename

def save_uploaded_file(file):
    upload_folder = "uploads/raw_data"

    # Agar folder nahi hai to bana do
    os.makedirs(upload_folder, exist_ok=True)

    # File ka naam lo
    filename = secure_filename(file.filename)

    # Complete path banao
    file_path = os.path.join(upload_folder, filename)

    # Save karo
    file.save(file_path)

    return file_path