# Utility functions for working with datasets from
# NCBI Gene Expression Omnibus (GEO).

import glob
from pathlib import Path

def find_prefix(path: str, suffixes):
    if len(suffixes) < 1:
        raise Exception("At least one suffix must be provided.")

    shared_prefix = None

    for suffix in suffixes:
        matches = glob.glob(f"{path}/*{suffix}")

        if len(matches) == 0:
            raise Exception(f"No file in `{path}` matched suffix `{suffix}`.")

        if len(matches) > 1:
            raise Exception(f"More than one file in `{path}` with suffix `{suffix}`.")
        
        prefix = matches[0][len(path) + 1:-len(suffix)] # strip off suffix

        if shared_prefix is None:
            shared_prefix = prefix

        if prefix != shared_prefix:
            raise Exception(f"File with suffix `{suffix}` has a different"
                             " prefix than the shared prefix `{shared_prefix}`")

    return shared_prefix
    

def find_10x_mtx_prefix(path):
    return find_prefix(
            path,
            ("barcodes.tsv.gz", "matrix.mtx.gz", "features.tsv.gz"))

