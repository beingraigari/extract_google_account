

import glob
import shutil
import os
import time

program_start = time.time()

src_dir = "C:\GExports"
dst_dir = "C:\GExtracts_MP4"
for mp4file in glob.iglob(os.path.join(src_dir, "\**\*.jpg"), recursive=True):
    # print({jpgfile})
    shutil.copy(mp4file, dst_dir)

program_end = time.time()

print("Time taken to execute this program :", (program_end-program_start) * 10**3, "ms")