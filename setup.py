from setuptools import find_packages,setup
from typing import List
minus_hypen_dot="-e."

def get_requirement(path:str)->list[str]:
    required=[]
    with open(path) as file_obj:
        required=file_obj.readlines()
        required=[req.replace("\n","") for req in required]
        if minus_hypen_dot in required:
            required.remove(minus_hypen_dot)
        return required

setup(
    name="Diamond price prediction",
    version='0.0.1',
    author="Gaurav jangid",
    author_email="gauravjangid341542",
    install_requires=get_requirement("/Users/gauravjangid/Desktop/project/MACHINE LEARNING/Diamond price prediction/requirement.txt"),
    packages=find_packages()
)