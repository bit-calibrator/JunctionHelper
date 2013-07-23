import os
import shutil
from ntfsutils import junction

def move_and_junction(src,dest):
    shutil.move(src,dest)
    junction.create(dest, src) 
    