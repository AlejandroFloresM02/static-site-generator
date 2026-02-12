from copystatic import copy_static_files
from getcontent import generate_page, generate_pages_recursive


def main():
    copy_static_files("static", "public")
    generate_pages_recursive("content", "template.html", "public")


main()
