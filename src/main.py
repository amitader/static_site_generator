import os
import shutil
import sys
from copystatic import transfer_dir
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_docs ="./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    try:
        basepath=sys.argv[1]
    except:
        basepath="/"
    print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    transfer_dir(dir_path_static,dir_path_docs)

    print("Generating page...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)


    

if __name__=="__main__":
    main()