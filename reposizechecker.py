from pathlib import Path
def get_path_size(path = Path('.'), recursive=False):
    """
    Gets file size, or total directory size

    Parameters
    ----------
    path: str | pathlib.Path
        File path or directory/folder path

    recursive: bool
        True -> use .rglob i.e. include nested files and directories
        False -> use .glob i.e. only process current directory/folder

    Returns
    -------
    int:
        File size or recursive directory size in bytes
        Use cleverutils.format_bytes to convert to other units e.g. MB
    """
    path = Path(path)
    if path.is_file():
        size = path.stat().st_size
    elif path.is_dir():
        path_glob = path.rglob('*.*') if recursive else path.glob('*.*')
        size = sum(file.stat().st_size for file in path_glob)
    return size


def humanbytes(B):
    """Return the given bytes as a human friendly KB, MB, GB, or TB string."""
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2) # 1,048,576
    GB = float(KB ** 3) # 1,073,741,824
    TB = float(KB ** 4) # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B / KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B / MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B / GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B / TB)

print("""
Repostiory Size Checker

Total Size: {}
""".format(humanbytes(get_path_size(Path('.'), recursive=True))))