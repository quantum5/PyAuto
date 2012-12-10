#!/usr/bin/env python
import ez_setup
ez_setup.use_setuptools()
from setuptools import setup

setup(name='PyAuto',
      version='0.0.0',
      description='Automate GUI Application',
      author='Xiaomao Chen',
      author_email='xiaomao5@live.com',
      #url='',
      packages=['pyauto'],
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: System Administrators',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python',
          'Topic :: Home Automation',
          'Topic :: System :: Systems Administration',
          'Topic :: Utilities',
          ],
     )
