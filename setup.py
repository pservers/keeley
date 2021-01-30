# encoding: utf-8

from setuptools import setup


def install_data_files_hack():
    # This is a clever hack to circumvent distutil's data_files
    # policy "install once, find never". Definitely a TODO!
    # -- https://groups.google.com/group/comp.lang.python/msg/2105ee4d9e8042cb
    from distutils.command.install import INSTALL_SCHEMES

    for scheme in INSTALL_SCHEMES.values():
        scheme["data"] = scheme["purelib"]


install_data_files_hack()

requires = [
    "flask",
    "httpauth",
    "humanize",
]

setup(
    name="keeley",
    version="0.0.1",
    author="Fpemud",
    author_email="fpemud@sina.com",
    packages=["keeley"],
    scripts=["bin/keeley"],
    include_package_data=True,
    zip_safe=False,
    url="https://github.com/pservers/keeley",
    description="A simple and easy-to-set-up web file manager that Just Works™.",
    long_description=__doc__,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Software Development :: Version Control",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=requires,
)
