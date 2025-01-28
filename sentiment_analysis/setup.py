from setuptools import setup, find_packages

setup(
    name='sentiment-analysis-api',
    version='0.1',
    description='API for Sentiment Analysis using HuggingFace Model',
    author='Your Name',
    author_email='your-email@example.com',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'transformers',
        'torch',
        'prometheus-fastapi-instrumentator',
        'requests',
        'pydantic',
        'gitpython',
    ],
)
