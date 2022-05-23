import os


def main():
    """
    Be very careful in inputting correct path for main_dir - because this program will rename files recursively.
    With wrong path, your file sytem will get corrupted.  This method is going to rename all files within the
    main directory path that got entered as main_dir to .jpg files.  This means, if the files within the main_dir
    aren't jpg type, these files will still be renamed to jpg files.
    :return:
    """
    main_dir = 'C:/Users/argda/PycharmProjects/RenameFilesInBulk/photos/'
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
