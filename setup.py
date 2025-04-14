from setuptools import find_packages,setup
from typing import List

#Creating function takes the path of requirements and should be able to read
#all the libraries available should get installed

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]: 
    ''' This function will return the list of requirements
    '''
    requirements=[]                         # Initialising a list
    with open(file_path) as file_obj:     # Creating temporary file objects
        requirements=file_obj.readlines()   # This will read the lines inside requirements 
        [req.replace("\n","")for req in requirements]  
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
            
    return requirements                   #

setup(
name='mlproject',
version='0.0.1',
author='Sankalp',
author_email='sankalp.dangwal@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)