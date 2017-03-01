from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name = 'Minihash',
      version = '0.1',
      description = 'Recursively traverse directories and take file HMAC-SHA1 calculations.',
      long_description = readme(),
      classifiers = [
          'Programming Language :: Python :: 3.4',
          'License :: OSI Approved :: GPLv3',
          'Development Status :: under constant development through feedback',
      ],
      author = 'Neville Tummon',
      license = 'GPLv3',
      include_package_data = True,
      zip_safe = False)
