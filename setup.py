from setuptools import setup
with open("README.rst", "rb") as f:
    long_descr = f.read().decode('utf-8')

with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name="LyricsXtractor",
    version="1.1.3",
    description='A tool to obtain the lyrics to your favorite songs',
    author='Sairam Padhy',
    author_email='sairampadhy07@gmail.com',
    url='https://github.com/VamosRafa07/getlyrics',
    long_description=long_descr,
    license='MIT',
    packages=["getlyrics"],
    install_requires=requirements,
    entry_points= {
        "console_scripts" : ['lyrics-dl=getlyrics.__main__:maingl']
    }
)
