import os
from ntfsutils import junction

def move_and_junction(src,dest):
    os.rename(src,dest)
    junction.create(src,dest) 
    