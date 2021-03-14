from setuptools import setup, find_packages

setup(
    name='didmap-client-back',
    version='1.0',
    description="Unofficial Python Api client for https://mapasinteractivos.didactalia.net",
    author="Jose Blanco Perales",
    author_email='jblanpere@gmail.com',
    license="GPL",
    url="https://github.com/jblanper/didmap-client-back",
    packages=find_packages(),
    install_requires=["requests", "rdflib", "fastapi", "uvicorn", "SPARQLWrapper"],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'start-dev=didmap_api.dev_server:main',
        ],
    },
)