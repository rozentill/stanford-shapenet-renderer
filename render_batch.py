import os
import sys
import time
from joblib import Parallel, delayed
import argparse


def render(dst, item_id):

	f_out = dst
	f_item = item_id
	os.system(
		'blender --background --python render_custom.py -- --output_folder %s --item %s' % (f_out, f_item)
	)

def main():

	dst = 'D:/Data/ShapeNetRendering_high\\03001627'
	items_list = os.listdir('D:\\Data\\shapenetrendering_compressed\\ShapeNetRendering\\ShapeNetRendering\\03001627')
	with Parallel(n_jobs=4) as parallel:
		parallel(delayed(render)(dst, item_id) 
			for item_id in items_list)
	

if __name__ == '__main__':

	main()