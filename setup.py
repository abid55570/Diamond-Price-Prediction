from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

# hypen e dot is used when used to install using requirements.txt (pip install requiremets.txt in terminal) mentioning -e . in the requiremets.txt file 
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements
    
# to run the setup.py file run in terminal ==>> python setup.py install

setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    aurthor='Abid',
    aurthor_email='abid.aslam55570@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)