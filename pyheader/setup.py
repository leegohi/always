
from setuptools import (
    find_packages,
    setup,
)
from pyheader import WIN 

def install_requires():
    if WIN:
        return ["pywin32"]
    return []
setup(
    name='pyheader',
    url="""https://zhuanlan.zhihu.com/c_208876015
           https://github.com/leegohi/always.git
        """,
    version="1.0",
    description='A headers tools for spider.',
    entry_points={
        'console_scripts': [
            'pyheader = pyheader.header2dict:main',
        ],
    },
    author='walle',
    author_email='walle88@qq.com',
    packages=find_packages(),
    install_requires=install_requires(),
    include_package_data=True,
    license='Apache 2.0',
    classifiers=[
        'Development Status :: Beta',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Intended Audience :: Spider',
    ],
)