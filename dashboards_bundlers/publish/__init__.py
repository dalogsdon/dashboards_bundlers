# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from ..server_upload import bundle as upload_bundle

def bundle(handler, abs_nb_path):
    upload_bundle(handler, abs_nb_path, True)
