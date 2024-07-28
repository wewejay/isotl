import os.path

import click


def index(path: str):
    """
    Index an ISO files
    :param path:
    :return:
    """

    iso_abs_path_list = []
    abs_path = os.path.abspath(path)
    if os.path.isfile(abs_path):
        iso_abs_path_list.append(abs_path)
    elif os.path.isdir(abs_path):
        iso_abs_path_list = [os.path.join(abs_path, f) for f in os.listdir(abs_path) if f.endswith('.iso')]
    else:
        raise ValueError(f"Invalid path: {abs_path}")

