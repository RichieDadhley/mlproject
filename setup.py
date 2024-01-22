from setuptools import find_packages,setup
from typing import List

hyphen_e_dot = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if hyphen_e_dot in requirments:
            requirments.remove(hyphen_e_dot)

    return requirments


setup(
    name = 'mlproject',
    version ='0.0.1',
    author = 'Richie',
    author_email = 'richie.s.dadhley@gmail.com',
    packages =find_packages(),
    # install_requires: provide a list of the packages you need, this will install all those libraries automatically. 
    # Here we use a function as we will need many packages.
    install_requires = get_requirements('requirements.txt')
)