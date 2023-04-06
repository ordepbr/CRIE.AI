from setuptools import setup, find_packages

setup(
    name='CRIE.AI',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.20.3',
        'tensorflow==2.11.1',
        'tensorrt==8.0.1',
        'opencv-python==4.5.4.58',
        'scikit-learn==1.0.2',
        'matplotlib==3.5.1'
    ],
    python_requires='>=3.11'
)
