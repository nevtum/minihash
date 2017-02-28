
import fnmatch
import hashlib
import hmac
import os
import sys

# Limited to small files. Currently cannot handle large files
def hmac_sha(filename, key=""):
    file = open(filename, 'rb')
    try:
        body = file.read()
    finally:
        file.close()

    seed = key.encode('utf-8')
    digest = hmac.new(seed, body, hashlib.sha1).hexdigest()
    return digest

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

def main():
    if (len(sys.argv) < 2):
        print("Usage: {0} filepath".format(sys.argv[0]))
        sys.exit(1)

    for filepath in find_files(sys.argv[1], '*'):
        print("{0}, {1}".format(hmac_sha(filepath), filepath))

if __name__ == '__main__':
    main()
