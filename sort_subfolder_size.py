import argparse
import os
import os.path

parser = argparse.ArgumentParser(description="list sub-folder's size")
parser.add_argument("folder", help='the folder you want to evaluate')
args = parser.parse_args()
fileSize = {}

suffix = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
def convert_byte(size):
    '''Convert a byte number to human-readable form.
    Keyword arguments:
    size: input a byte number
    Returns: string
    '''
    if size<0:
        raise ValueError('number must be non-negative')
    for suf in suffix:
        size /= 1024
        if size < 1024:
            return '{0:.1f} {1}'.format(size, suf)
    raise ValueError('number too large')
def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        #get child files size
        for child_file in files:
            size += os.path.getsize(os.path.join(root, child_file))
        #get child dir size
        for child_dir in dirs:
            size += getdirsize(os.path.join(root, child_dir))
    return size

if not os.path.exists(args.folder):
    raise Exception("the folder doesn't exist")
else:
    subs = os.listdir(path=args.folder)
    for ele in subs:
        fullPath = os.path.join(args.folder, ele)
        if os.path.isfile(fullPath):
            fileSize[os.path.getsize(fullPath)] = fullPath
        elif os.path.isdir(fullPath):
            fileSize[getdirsize(fullPath)] = fullPath

    for size in sorted(fileSize, reverse=True):
        print(fileSize[size] + ' ' + convert_byte(size))
