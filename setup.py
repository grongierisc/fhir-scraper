import setuptools 
 
setuptools.setup(
    name='fhir-scraper',    # This is the name of your PyPI-package.
    version='0.1',                          # Update the version number for new releases
    scripts=['src/app'],                  # The name of your scipt, and also the command you'll be using for calling it
    python_requires='>=3.6.6',
    author="Guillaume Rongier",
    author_email="guillaume.rongier@intersystems.com",
    url="https://www.intersystems.com/",
    description="A simple python script to copy/scrap/crawl a FHIR repository to another one.", 
)