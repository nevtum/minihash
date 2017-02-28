
import fnmatch, hmac, hashlib, sys, os

def hmac_sha(filename, key = ""):
    f = open(filename, 'rb')
    try:
        body = f.read()
    finally:
        f.close()

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
    for filepath in find_files('.', '*'):
        print("{0}, {1}".format(hmac_sha(filepath), filepath))

if __name__ == '__main__':
    main()
