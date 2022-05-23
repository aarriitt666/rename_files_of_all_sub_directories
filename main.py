import os


def main():
    """
    Be very careful in inputting path for main_dir - because this program will rename files recursively, but
    only one level deep.  So make sure the path of directory you want this script to run on is the intended one.

    For example: this script will rename all files including directories in any sub directory of
    the main directory -- such as files 1, 2, 3 in photos/a and files 4, 5, 6 in photos/b will be renamed to a_1.jpg,
    a_2.jpg, a_3.jpg in photos/a and b_4.jpg, b_5.jpg, b_6.jpg in photos/b.  Caution:  If the files within the main_dir
    aren't jpg type, these files will still be renamed to jpg files.
    :return:
    """
    main_dir = 'C:/Users/blahblahblahblah/PycharmProjects/RenameFilesInBulk/photos/'
    sub_dirs = [dir_name for dir_name in os.listdir(main_dir) if os.path.isdir(os.path.join(main_dir, dir_name))]
    new_sub_dirs = []
    ignore_dirs = ['.idea', 'env']
    for i in sub_dirs:
        if i in ignore_dirs:
            pass
        else:
            new_sub_dirs.append(i)

    for i in new_sub_dirs:
        for count, filename in enumerate(os.listdir(f'{main_dir}/{i}'), start=1):
            file_prefix = f'{new_sub_dirs[new_sub_dirs.index(i)]}'
            dst = f'{file_prefix}_{str(count)}.jpg'
            src = f'{main_dir}/{i}/{filename}'
            dst = f'{main_dir}/{i}/{dst}'
            os.rename(src, dst)


if __name__ == '__main__':
    main()
