import os
import random
from typing import List


def weird_file_handler(dir_path: str, no_files: int) -> str:
    """
    Create `no_files` files inside `dir_path`, delete half randomly,
    write content to the remaining files, and return a list with the
    length (no. of characters) in each remaining file

    :param dir_path: Directory path where files will be created
    :type dir_path: str

    :param no_files: Number of files to create
    :type no_files: int

    :return: List with lengths of remaining files
    :rtype: List[int]
    """

    path = os.path.abspath(dir_path)
    if not os.path.exists(path):
        os.makedirs(path)

    for i in range(no_files):
        fname = os.path.join(path, f"file_{i}.txt")
        open(fname, "w").close()

    files = [
        os.path.join(path, f)
        for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    ]

    to_delete = len(files) // 2
    for _ in range(to_delete):
        chosen = random.choice(files)
        try:
            os.remove(chosen)
        except FileNotFoundError:
            print(f"File {chosen} not found for deletion.")
            continue

        if chosen in files:
            files.remove(chosen)

    lengths = []
    for fpath in files:
        lines_to_write = random.randint(1, 10)
        with open(fpath, "w+") as f:
            for j in range(lines_to_write):
                f.write(f"Line {j+1} for {os.path.basename(fpath)}\n")
            f.seek(0)
            contents = f.read()
            lengths.append(len(contents))

    return f"File Handling Complete.\nLengths of remaining files: {lengths}"


def main() -> None:
    print(weird_file_handler("test_dir", 10))


if __name__ == "__main__":
    main()
