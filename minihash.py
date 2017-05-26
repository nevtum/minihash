
import fnmatch
import hashlib
import hmac
import os
import sys

def hmac_sha1(filename, key=""):
    seed = key.encode('utf-8')
    sig = hmac.new(seed, None, hashlib.sha1)
    for chunk in chunks(filename):
        sig.update(chunk)
    return sig.hexdigest()

def sha1(filename):
    sig = hashlib.sha1()
    for chunk in chunks(filename):
        sig.update(chunk)
    return sig.hexdigest()

def chunks(filename):
    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(1024)
            if not chunk:
                break
            yield chunk

def find_files(directory, pattern):
    for root, _, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

def main():
    if len(sys.argv) < 2:
        print("Usage: {0} root-dir".format(sys.argv[0]))
        sys.exit(1)

    for filepath in find_files(sys.argv[1], '*'):
        try:
            print("hmac-sha1: {0}, filepath: {1}".format(hmac_sha1(filepath), filepath))
        except:
            print("Could not generate hash for %s" % filepath)
        # print("sha1: {0}, filepath: {1}".format(sha1(filepath), filepath))

if __name__ == '__main__':
    main()
