"""
setup.py for be-bi-application-frame.

If you are using this code as a bolierplate, remember to
update the information contained here to match your project!

For reference see
https://packaging.python.org/guides/distributing-packages-using-setuptools/

"""
from pathlib import Path
from setuptools import setup, find_packages


HERE = Path(__file__).parent.absolute()
with (HERE / 'README.md').open('rt') as fh:
    LONG_DESCRIPTION = fh.read().strip()

REQUIREMENTS: dict = {
    'core': [
        "pyqt5",
        "pyqtgraph",
        "pyjapc>=2.0.7",  # Necessary because of comrad atm
        "papc",  # For the sandbox mode
        "be-bi-application-frame",
        "comrad",
        "accwidgets",  # For the plots
    ],
    'test': [
        "pytest",
        "pytest-qt",
        "pytest-cov",
        "pytest-random-order",
        "papc",  # For the sandbox mode
    ],
    'dev': [
    ],
    'doc': [
        # 'sphinx',
    ],
}

setup(
    name='be-bi-pyqt-template',  # Your application name
    version="0.0.1.dev1",  # The latest version of this package

    author="Sara Zanzottera",  # Your name
    author_email="sara.zanzottera@cern.ch",  # Your email
    description="BE BI PyQt Template",  # Your project's short description
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='',

    packages=find_packages(),
    python_requires='>=3.6, <4',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],

    install_requires=REQUIREMENTS['core'],
    extras_require={
        **REQUIREMENTS,
        # The 'dev' extra is the union of 'test' and 'doc', with an option
        # to have explicit development dependencies listed.
        'dev': [req
                for extra in ['dev', 'test', 'doc']
                for req in REQUIREMENTS.get(extra, [])],
        # The 'all' extra is the union of all requirements.
        'all': [req for reqs in REQUIREMENTS.values() for req in reqs],
    },
    entry_points={
        'console_scripts': [
            # MODIFY: remove this line and add a pointer to the startup function of your app.
            # This means: 'example-app' launches "be_bi_pyqt_template/main.py:main()"
            'example-app=be_bi_pyqt_template.main:main',
        ],
    },
)
