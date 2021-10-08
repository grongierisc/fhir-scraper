import setuptools  
from setuptools.command.install import install

setuptools.setup(
    name='fhir-scraper',    # This is the name of your PyPI-package.
    version='0.1',                          # Update the version number for new releases
    scripts=['src/fhir-scraper.py'],                  # The name of your scipt, and also the command you'll be using for calling it
    python_requires='>=3.6.2',
    author="Guillaume Rongier",
    author_email="guillaume.rongier@intersystems.com",
    url="https://github.com/grongierisc/fhir-scraper",
    description="A simple python script to copy/scrap/crawl a FHIR repository to another one.", 
    install_requires=[
        'aiohttp==3.7.4.post0',
        'async-timeout==3.0.1',
        'attrs==21.2.0',
        'certifi==2021.5.30',
        'chardet==4.0.0',
        'charset-normalizer==2.0.6',
        'fhirpy==1.2.1',
        'idna==3.2',
        'idna-ssl==1.1.0',
        'multidict==5.2.0',
        'pytz==2021.3',
        'requests==2.26.0',
        'typing-extensions==3.10.0.2',
        'urllib3==1.26.7',
        'yarl==1.7.0'
    ],
)
