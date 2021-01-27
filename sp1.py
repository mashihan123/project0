import dask.bag as db
import dask.dataframe as dd
import json
import dask
import dask.array as da
import os
from dask.distributed import Client, progress
from dask import delayed

# a = db.read_text(['/Users/mashi/Desktop/project0/handout/data/4300-0.txt',
#                  '/Users/mashi/Desktop/project0/handout/data/pg36.txt',
#                  '/Users/mashi/Desktop/project0/handout/data/pg514.txt',
#                  '/Users/mashi/Desktop/project0/handout/data/pg1497.txt',
#                  '/Users/mashi/Desktop/project0/handout/data/pg3207.txt',
#                  '/Users/mashi/Desktop/project0/handout/data/pg6130.txt',
#                  '/Users/mashi/Desktop/project0/handout/data/pg19033.txt',
#                  '/Users/mashi/Desktop/project0/handout/data/pg42671.txt'])

a = db.read_text('/Users/mashi/Desktop/project0/handout/data/4300-0.txt').to_dataframe()

