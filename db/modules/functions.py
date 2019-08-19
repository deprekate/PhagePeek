import os
import argparse
from argparse import RawTextHelpFormatter

def is_valid_file(x):
	if not os.path.exists(x):
		raise argparse.ArgumentTypeError("{0} does not exist".format(x))
	return x

def get_args():
	usage = 'clean_database.py [-opt1, [-opt2, ...]] infile'
	parser = argparse.ArgumentParser(description='A program to clean fasta formatted sequence databases', formatter_class=RawTextHelpFormatter, usage=usage)
	parser.add_argument('infile', type=is_valid_file, help='input file in fasta format')
	#parser.add_argument('-o', '--outfile', action="store", default=sys.stdout, type=argparse.FileType('w'), help='where to write the output [stdout]')
	#parser.add_argument('-f', '--outfmt', action="store", default="tabular", dest='outfmt', help='format of the output [tabular]', choices=['tabular','genbank','fasta'])
	#parser.add_argument('-d', '--dump', action="store_true")
	parser.add_argument('-i', '--include', action="store", default="", dest='good_term', help='sequence read header must contain this string')
	parser.add_argument('-e', '--exclude', action="store", default="xxx", dest='bad_term', help='sequence read header must NOT contain this string')
	args = parser.parse_args()
	return args
