import sys
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

gene_name = sys.argv[1]

urllib.request.urlretrieve("https://www.uniprot.org/uniprot/?query=" + gene_name + "&format=fasta&compress=yes", gene_name + ".fasta.gz")
