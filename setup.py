import os
from setuptools import setup, find_packages

with open(os.path.join('drf_multiple_serializer', '__init__.py')) as f:
    for line in f:
        if line.startswith('__version__ ='):
            version = line.split('=')[1].strip().strip('"\'')

with open(os.path.join('README.md')) as f:
    long_description = f.read()

setup(
    name='drf-multiple-serializer',
    version=version,
    license="MIT",
    description='Django REST framework serializer utility',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='jay kim',
    author_email='jaykim1361@gmail.com',
    url='https://github.com/qpfmtlcp/drf-multiple-serializer',
    packages=find_packages(),
    install_requires=[
        'Django>=1.11',
        'djangorestframework>=3.8',
    ],
    keywords=['django', 'drf', 'serializer'],
    python_requires='>=3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ]
)
