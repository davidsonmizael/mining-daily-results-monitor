try: 
    from setuptools import setup
except ImportError:
    from distutils.core import setup

dependencies = [
    'python-dotenv',
    'pyyaml',
    'requests',
    'gspread',
    'oauth2client',
    'google-api-python-client',
    'numpy',
    'cython',
    'pandas'
]

dev_dependencies = [
    'pytest'
]

kwargs = dict(
    name='Monitoring tool for mining progress',
    description="Monitoring tool created to monitor the daily progress while mining on flexpool",
    version='0.1',
    author='Davidson Mizael',
    author_email='davidsonmizael@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.6, <4',
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        dev=dev_dependencies,
    )
)

if __name__ == '__main__':
    setup(**kwargs)