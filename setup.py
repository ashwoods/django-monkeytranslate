
import os
import codecs
from setuptools import setup


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


setup(
    name="monkeytranslate",
    version="0.0.1b",
    url='https://github.com/ashwoods/django-monkeytranslate',
    license='BSD',
    description="Monkeypatch django do-translation",
    long_description=read('README.rst'),
    author='Ashley Camba Garrido',
    author_email='ashwoods@gmail.com',
    packages=['monkeytranslate'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],
)
