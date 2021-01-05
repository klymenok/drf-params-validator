import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drf-action-params-validator",
    version="0.0.3",
    author="Oleksii Klymenok",
    author_email="klymenok.a@gmail.com",
    description="A small validator for params in drf view actions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/klymenok/drf-params-validator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
    'Django>=2.2.0',
    'djangorestframework>=3.11.0'
    ]
)
