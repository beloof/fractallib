from setuptools import setup, find_packages

setup(
    name='fractallib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'tqdm'
    ],
    description='A package to generate Mandelbrot and Julia fractals',
    author='LASSIOUED Badis',
    author_email='lassiouedbadiss@yahoo.com',
    url='https://github.com/beloof/fractallib',
    license="MIT",
    entry_points={
        "console_scripts": [
            "fractallib=fractallib.__main__:main",
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)


