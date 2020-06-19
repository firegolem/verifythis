import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Verify This Info", # Replace with your own username
    version="0.1",
    author="Aditya V R R",
    author_email="aditya.vrr@gmail.com",
    description="Verify news from social media forwards on whatsapp/telegram and other networking apps",
    long_description=long_description,
    url="https://github.com/firegolem/verifythis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
