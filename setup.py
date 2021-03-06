from setuptools import setup, find_packages


setup(
    name='django-crequest',
    version=".".join(map(str, __import__('crequest').__version__)),
    description='Middleware to make current request always available.',
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    url='https://github.com/Alir3z4/django-crequest',
    packages=find_packages(exclude=['django_crequest']),
    install_requires=['Django>=1.2'],
    keywords=[
        'django',
        'request',
        'web'
    ],
    platforms='OS Independent',
    provides=['crequest',],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Development Status :: 6 - Mature",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
    ],
)
