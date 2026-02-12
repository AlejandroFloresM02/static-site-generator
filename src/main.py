import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    print("Deleting public directory...")
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path, basepath)
    print("Done!")


main()
