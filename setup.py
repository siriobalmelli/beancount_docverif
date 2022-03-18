from os import path
from setuptools import find_packages, setup

with open(path.join(path.dirname(__file__), 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='beancount_docverif',
    version="1.0.1",
    py_modules=["beancount_docverif"],

    description='Document verification plugin for Beancount',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',

    setup_requires=[
        'setuptools_scm'
    ],
    install_requires=[
        'beancount',
    ],
    extras_require={
        'dev': [
            'pytest',
            'tox'
        ]
    },
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,  # cargo cult moment: interwebz sez to write this

    url='https://github.com/siriobalmelli/beancount_docverif',
    author='Sirio Balmelli',
    author_email='sirio@b-ad.ch',
    license='MIT',
    keywords='plugins double-entry beancount accounting document verification',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Topic :: Office/Business :: Financial :: Investment',
    ],
)
