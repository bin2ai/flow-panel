from setuptools import setup, find_packages

setup(
    name='flow_panel',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pymupdf==1.24.9',
    ],
    entry_points={
        'console_scripts': [
            # Define command-line scripts here, if any
            'your_command=your_module.main:main_function',
        ],
    },
    # Optional fields
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bin2ai/flow-panel',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
