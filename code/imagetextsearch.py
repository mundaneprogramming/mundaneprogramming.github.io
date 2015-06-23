from PIL import Image
import argparse
import pytesseract
import os
import re

IMAGE_FN_PATTERNS = ('jpg', 'jpeg', 'gif', 'tif', 'png', 'tiff', 'bmp')
# for root, subdirs, files in os.walk(rootdir):


def extract_text(fname):
    img = Image.open(fname)
    return pytesseract.image_to_string(img)


def find_image_filenames(rootdir, fnpatterns = IMAGE_FN_PATTERNS):
    fnames = []
    for root, subdirs, filenames in os.walk(rootdir):
        for fn in filenames:
            if fn.lower().endswith(fnpatterns):
                p = os.path.join(root, fn)
                fnames.append(p)
    return fnames


def find_patterns_by_line(txtstring, patterns):
    results = []
    rxpatterns = [re.compile(p, re.IGNORECASE) for p in patterns]
    for linenum, line in enumerate(txtstring.splitlines()):
        for rx in rxpatterns:
            match = re.search(rx, line)
            if match:
                s = match.span()
                results.append({
                    'linenum': linenum,
                    'match': line[s[0]:s[1]],
                    'line': line
                })

    return results




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--show-nulls", '-s', action = 'store_true',
        default = True,
        help = "Output found and translated images, even if no match is found.")
    parser.add_argument("path", nargs = 1,
            help = "Path to start searching")
    parser.add_argument("patterns", nargs = '*',
        help = "Text patterns to search for")

    args = parser.parse_args()
    rootpath = args.path[0]
    patterns = args.patterns

    for fname in find_image_filenames(rootpath):
        txt = extract_text(fname)
        matches = find_patterns_by_line(txt, patterns)
        if not matches:
            if args.show_nulls:
                print("\n-{fn}\n\tNO MATCH in {c} chars".format(
                    fn = fname, c = len(txt)))

        else:
            print("\n-", fname)
            for d in matches:
                print("\t{lno}:\t{mtch}::\t{line}".format(
                        lno = d['linenum'],
                        mtch = d['match'], line = d['line'].strip()
                    ))
