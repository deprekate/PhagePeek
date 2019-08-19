import sys
import os
import re
import warnings

#sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/lib')
from modules.functions import functions

from ete3 import NCBITaxa
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

ncbi = NCBITaxa()
#print(dir(ncbi))

#id = '318419'
#lineage = ncbi.get_lineage(id)
#names = ncbi.get_taxid_translator(lineage)
#print( [names[taxid] for taxid in lineage] )
#exit()

class SequenceRead:
	"""A single equence read class"""
	head = ''
	data = ''
	def __repr__(self):
		return self.head + self.data

args = functions.get_args()

def sequence_good(seq):
	match = uniprot_ox.search(seq.head)
	if match:
		try:
			ncbi_lineage = ncbi.get_lineage(match.group(1))
			ncbi_names = ncbi.get_taxid_translator(ncbi_lineage)
			ncbi_name = ncbi_names[ncbi_lineage[2]]
			# prokaryotic
			if ncbi_name in ('Bacteria', 'Archaea', 'Caudovirales', 'unclassified bacterial viruses', 'unclassified archaeal viruses'):
				return True
		except ValueError as e:
			warnings.warn(str(e))
			pass
	return False

uniprot_ox = re.compile('OX=(\d+)')

seq = SequenceRead()
with open(args.infile) as f:
	for line in f:
		if line.startswith('>'):
			if args.good_term.upper() in seq.head.upper() and not args.bad_term.upper() in seq.head.upper() and sequence_good(seq):
				print(seq)
			seq.head = line
			seq.data = ''
		else:
			seq.data += line
			
