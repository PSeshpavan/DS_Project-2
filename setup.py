from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
    """
    This function returns a list of requirements.
    """
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
        


setup(
    name="DS_Project-2",
    version="0.0.1",
    author="Pavan",
    author_email="pseshpavan@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
    