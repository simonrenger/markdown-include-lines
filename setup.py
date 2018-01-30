from setuptools import setup, find_packages

setup(
  name = 'markdown-include-lines',
  packages = find_packages(),
  version = '1.0',
  description = 'This extension allows you to include lines or a whole source file into your file. The syntax of the markdown is like this: {python 1-9 test.py} or the whole file {python * include.py}',
  long_description = "",
  author = 'Simon Renger',
  author_email = 'info@simonrenger.de',
  url = 'https://github.com/simonrenger/markdown-include-lines', 
  download_url = 'https://github.com/simonrenger/markdown-include-lines',
  keywords = ['Markdown', 'typesetting', 'include', 'plugin', 'extension','lines'],
  install_requires = ['markdown']
)
