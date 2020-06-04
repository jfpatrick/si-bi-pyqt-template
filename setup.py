"""
setup.py for be-bi-pyqt-template.

If you are using this code as a boilerplate, remember to
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
        "pyqt5ac @ git+https://:@gitlab.cern.ch:8443/szanzott/pyqt5ac.git",  # To automate the compilation of .ui and .qrc files
        "pyqtgraph",
        "be-bi-application-frame",
        "comrad",  # FIXME Provides the CLogDisplay, remove in favor of the real AppFrame or accwidgets'version when out
        "accwidgets",  # For the plots
        "pyjapc==2.1.2",  # FIXME Has to go after comrad to pick the right version?
        "importlib-metadata==1.0.0",  # FIXME Due to comrad I suppose?
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
        'sphinx',
        'acc-py-sphinx',
    ],
}

setup(
    name='be-bi-pyqt-template',  # Your application name
    version="0.0.1.dev1",  # The latest version of this package

    author="Sara Zanzottera",  # Your name
    author_email="sara.zanzottera@cern.ch",  # Your email
    description="BE BI PyQt Template Code",  # Your project's short description
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
    include_package_data=True,
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
            # This means: 'be-bi-pyqt-template' launches "be_bi_pyqt_template/main.py:main()"
            'be-bi-pyqt-template=be_bi_pyqt_template.main:main',
        ],
    },
)
