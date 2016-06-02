from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt", session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='tpDialler',
    version='0.1',
    py_modules=['tpDialler'],
    entry_points='''
        [console_scripts]
        tpDialler=tpDialler:make_call
    ''',
    install_requires=reqs
)
