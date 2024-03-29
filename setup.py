
# requirements
try:
  with open('requirements.txt') as f:
    reqs = f.read().splitlines()
except:
  reqs = []

import setuptools
with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'covid19czechia',
  version = '0.4.1',
  author = 'Martin Beneš',
  author_email = 'martinbenes1996@gmail.com',
  description = 'Web Scraper for Czechia COVID19 data.',
  long_description = long_description,
  long_description_content_type="text/markdown",
  packages=setuptools.find_packages(),
  license='MPL',
  url = 'https://github.com/martinbenes1996/covid19czechia',
  download_url = 'https://github.com/martinbenes1996/covid19czechia/archive/0.4.1.tar.gz',
  keywords = ['2019-nCov', 'czechia', 'coronavirus', 'covid-19', 'covid-data', 'covid19-data'],
  install_requires=reqs,
  package_dir={'': '.'},
  package_data={'': ['data/*.json','data/*.csv']},
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Developers',
    'Intended Audience :: Other Audience',
    'Topic :: Database',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Information Analysis',
    'Topic :: Software Development :: Libraries',
    'Topic :: Utilities',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)