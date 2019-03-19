from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="click-cli-news-api",
    version="1.0",
    author="Leni Kadali Mutungi",
    author_email="lenikmutungi@gmail.com",
    description="Commandline app that uses Click and News API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leni1/click-cli-news-api",
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary",
    ],
    keywords="click cli commandline news api",
    project_urls={
        'Source': 'https://github.com/leni1/click-cli-news-api',
    },
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=["Click", "requests", "python-dotenv", ],
    python_requires=">=3",
    entry_points={
        "console_scripts": [
            "news=client.cli:get_news_items"
        ]
    },
)
