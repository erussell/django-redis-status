from setuptools import setup, find_packages

setup(
    name='django-redis-status',
    version='1.0.6',
    description='A django application that displays the load and some other statistics about your redis cache instances in the admin.',
    long_description=open('README.md').read(),
    author='Eric Russell',
    author_email='erussell@ngs.org',
    url='http://github.com/erussell/django-redis-status',
    packages=find_packages(exclude=[]),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
