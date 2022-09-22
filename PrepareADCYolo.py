from math import factorial
import os
import glob
import shutil
import configparser
from cv2 import fastAtan2
from sklearn.model_selection import train_test_split


def scan_dirs_folder(folder):
    return [os.path.join(folder, d) for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]


def scan_files_subfolder(root_folder, search_exts):
    searched_files = []
    for root, dirs, files in os.walk(root_folder):
        for f in files:
            if any(f.endswith(ext) for ext in search_exts):
                searched_files.append(os.path.join(root, f))
    return searched_files


def scan_files_folder(root_folder, search_exts):
    files = [x for x in glob.glob(root_folder + '\\*.*') if any(x.endswith(ext) for ext in search_exts)]
    return files


def Main():
    oversampling = 1
    img_path_root = r'D:\BackendAOI\Data\DefectBoxDetection\2_PK5533\1'
    img_path_dst_train = r'train.txt'
    img_path_dst_valid = r'valid.txt'
    search_exts = ['jpg','jpeg', 'bmp', 'png']
    valid_keep_ratio = 0.2

    # check src folder
    if not os.path.isdir(img_path_root):
        print(img_path_root + ' is not exist!')
        return

    # split
    files = scan_files_subfolder(img_path_root, search_exts)
    files = files * oversampling
    train_files = files
    valid_files = []
    if valid_keep_ratio > 0:
        train_files, valid_files = train_test_split(files, test_size=valid_keep_ratio, random_state=42)
    print('train = ', train_files.__len__())
    print('valid = ', valid_files.__len__())

    # output train.txt
    with open(img_path_dst_train, 'w') as f:
        for name in train_files:
            print(name)
            f.write(f'{name}\n')

    # output valid.txt
    with open(img_path_dst_valid, 'w') as f:
        for name in valid_files:
            print(name)
            f.write(f'{name}\n')
    
    print('done')
    
if __name__ == '__main__':
    Main() 