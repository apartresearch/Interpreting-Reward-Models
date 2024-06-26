from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='reward_analyzer',
    version='0.9.0',
    packages=find_packages(),
    install_requires=requirements,
    author='Apart Research',
    author_email='amirabdullah19852020@gmail.com',
    description='Analyze internal reward models using sparse autoencoders.',
    url='https://github.com/apartresearch/Interpreting-Reward-Models',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
)
