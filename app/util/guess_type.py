import posixpath
import mimetypes


extensions_map = {
    '.gz': 'application/gzip',
    '.Z': 'application/octet-stream',
    '.bz2': 'application/x-bzip2',
    '.xz': 'application/x-xz',
}

def get_type(path) -> str:
    base, ext = posixpath.splitext(path)
    if ext in extensions_map:
        return extensions_map[ext]
    ext = ext.lower()
    if ext in extensions_map:
        return extensions_map[ext]
    guess, _ = mimetypes.guess_type(path)
    if guess:
        return guess
    return 'application/octet-stream'