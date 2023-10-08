import glob
import shutil
import os
import time

program_start = time.time()

src_dir = "C:\GExports"
dst_dir = "C:\GExtracts"
for jpgfile in glob.iglob(os.path.join(src_dir, "**\*.jpg"), recursive=True):
    print({jpgfile})
    shutil.copy(jpgfile, dst_dir)

program_end = time.time()

print("Time taken to execute this program :", (program_end-program_start) * 10**3, "ms")


# import os
# rootdir = 'C:/Users/sid/Desktop/test'

# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         print(os.path.join(subdir, file))