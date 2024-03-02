from docx2pdf import convert
import tempfile
import os
def converttopdf(input_file, ouptput_file):
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, input_file.name)
    with open(file_path, "wb") as f:
        f.write(input_file.getbuffer())
    convert(input_file.name, ouptput_file)
    return ouptput_file