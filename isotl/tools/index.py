import os.path
import time
from isotl import utils, db


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
    if not iso_abs_path_list:
        print("No ISOs found.")
        return
    print("Number of ISOs: {}".format(len(iso_abs_path_list)))

    while True:
        inp = input("q to quit, s to show all isos, c to continue: ").lower()
        if inp == 'q':
            print("Program terminated.")
            return
        elif inp == 's':
            for i in iso_abs_path_list:
                print(i)
        elif inp == 'c':
            break

    starttime = time.time()

    dbfile = "isotl.sqlite3"
    db_path = os.path.abspath(dbfile)

    print("DB File: {}".format(os.path.abspath(dbfile)))

    print("Start indexing...")

    db.db = utils.get_db(db_path)

    for iso_abs_path in iso_abs_path_list:
        print(f"Indexing {iso_abs_path}")
        utils.mount_win(iso_abs_path)