from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='pyAudioAnalysis',
    version='0.1-rayrrr',
    description='Python Audio Analysis Library: Feature Extraction, Classification, Segmentation and Applications',
    long_description='pyAudioAnalysis is a Python library covering a wide range of audio analysis tasks, including: feature extraction, classification, segmentation and visualization. This fork of a fork supports Python 3 and installation via `pip`.',
    url='https://github.com/tyiannak/pyAudioAnalysis',
    author='Theodoros Giannakopoulos',
    author_email='tyiannak@gmail.com',
    license='Apache 2.0',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],

    keywords='audio analysis feature extraction classification segmentation visualization',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    package_dir={'pyAudioAnalysis': 'pyAudioAnalysis'},
    package_data={'pyAudioAnalysis': ['data/svm*', 'data/gb*', 'data/et*', 'data/hmm*', 'data/knn*', 'data/rf*']},

    install_requires=['numpy', 'matplotlib', 'scipy', 'scikit_learn', 'hmmlearn', 'simplejson', 'eyeD3', 'six'],

    dependency_links=['git+ssh://git@github.com/rayrrr/pydub.git#egg=pydub']
)
