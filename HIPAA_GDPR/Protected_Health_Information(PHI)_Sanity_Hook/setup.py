from setuptools import setup, find_packages

setup(
    name="phi-sanity-hook",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "spacy>=3.0.0",
        "spacy-transformers>=1.1.0",
        "torch>=1.10.0",
    ],
    entry_points={
        "console_scripts": [
            "phi-scan=phi_sanity_hook.main:main",
        ],
    },
)