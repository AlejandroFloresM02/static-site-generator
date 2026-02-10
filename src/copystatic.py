import os
import shutil


def copy_static_files(src_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    items = os.listdir(src_dir)
    for item in items:
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        elif os.path.isdir(src_path):
            os.mkdir(dest_path)
            copy_static_files(src_path, dest_path)
        print(f"Copied {src_path} to {dest_path}")
