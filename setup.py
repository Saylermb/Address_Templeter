try:
    from setuptools import setup
except ImportError:
    raise ImportError("setuptools module required, please go to https://pypi.python.org/pypi/setuptools and follow the instructions for installing setuptools")

setup(
    version='1.02',
    url='',
    description='',
    name='address_templeter',
    packages=['address_templeter'],
    package_data={'address_templeter': ['learned_settings.crfsuite']},
    license='The MIT License: http://www.opensource.org/licenses/mit-license.php',
    install_requires=['python-crfsuite>=0.9.6',
                      'lxml'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Russian',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Linux :: Ubuntu',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis']
)
