from distutils.core import setup

setup(
    name='JunctionHelper',
    version='0.9.0',
    author='Michael Gassman',
    author_email='mike@bitcalibrator.com',
    packages=['junctionhelper'],
    scripts=['bin/move-and-junction.py'],
    url='http://bitcalibrator.com',
    license='LICENSE.txt',
    description='Common Junction use-cases',
    long_description=open('README.md').read(),
    install_requires=[
        "ntfsutils == 0.1.2",
    ],
)
