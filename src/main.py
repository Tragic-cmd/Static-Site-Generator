import os
import shutil
from textnode import TextNode, TextType

def main():
    copy_static_to_public()

def copy_static_to_public():
    stat_path = "/home/tragic/workspace/github.com/tragic-cmd/Static-Site-Generator/static"
    pub_path = "/home/tragic/workspace/github.com/tragic-cmd/Static-Site-Generator/public"

    if os.path.exists(pub_path):
        shutil.rmtree(pub_path)
    os.mkdir(pub_path)

    def copy_files(stat_path, pub_path):
        for item in os.listdir(stat_path):
            # Full path for the current item
            full_stat_path = os.path.join(stat_path, item)
            full_pub_path = os.path.join(pub_path, item)

            # You can now work with this path to determine if it's a file or directory
            if os.path.isfile(full_stat_path):
                shutil.copy(full_stat_path, full_pub_path)
            elif os.path.isdir(full_stat_path):
                # Make directory in destination if it doesn't exist
                if not os.path.exists(full_pub_path):
                    os.mkdir(full_pub_path)
                # Recursive call for directory
                copy_files(full_stat_path, full_pub_path)  # Modify to accept two paths
    # Start the copying process
    copy_files(stat_path, pub_path)


if __name__ == "__main__":
    main()