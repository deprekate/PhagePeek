import sys
import argparse
from argparse import RawTextHelpFormatter
import urllib.request

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

usage = 'download_uniprot.py [-opt1, [-opt2, ...]] gene_name'
parser = argparse.ArgumentParser(description='A program to ', formatter_class=RawTextHelpFormatter, usage=usage)
parser.add_argument('gene_name', type=str, help='The name of the gene')
args = parser.parse_args()

urllib.request.urlretrieve("https://www.uniprot.org/uniprot/?query=" + args.gene_name + "&format=fasta&compress=yes", args.gene_name + ".fasta.gz")
