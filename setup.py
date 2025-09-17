from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="spg-hackathon-2025",
    version="1.0.0",
    author="SPG Hackathon Team",
    author_email="team@spghackathon2025.com",
    description="AI-Driven Subsurface Data Analysis - SPG Hackathon 2025",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-team/spg-hackathon-2025",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": ["pytest", "black", "flake8", "pre-commit"],
        "viz": ["plotly", "bokeh", "seaborn"],
        "nlp": ["transformers", "spacy", "gensim"],
        "geo": ["obspy", "lasio", "welly"],
    },
    entry_points={
        "console_scripts": [
            "spg-process=src.data_processing.main:main",
            "spg-model=src.models.main:main",
        ],
    },
)
