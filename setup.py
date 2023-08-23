from setuptools import setup

setup(
    name='python-walmart-ad-api',
    version='0.1.1',
    install_requires=[
        "requests",
    ],
    packages=['ad_api', 'ad_api.api', 'ad_api.auth', 'ad_api.base']
    url='https://github.com/Lin1031/python-walmart-ad-api.git',
    license='MIT',
    author='Lin1031',
    author_email='lin1031@gmail.com',
    description='Python wrapper for the Walmart Advertising API'
)
