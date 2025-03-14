from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Author",
    author_email="author@example.com",
    description="A package for detecting emotions in text using Watson NLP API",
    keywords="emotion, detection, nlp, watson",
    python_requires=">=3.6",
)
