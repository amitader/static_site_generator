import os
import shutil
def transfer_dir(old_dir,new_dir):
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    for filename in os.listdir(old_dir):
        src_path=os.path.join(old_dir,filename)
        dest_path=os.path.join(new_dir,filename)
        print(f"transfering from: {src_path}\nto: {dest_path}")
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        else:
            os.mkdir(dest_path)
            transfer_dir(src_path,dest_path)