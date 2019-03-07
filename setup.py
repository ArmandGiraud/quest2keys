"""setting up package"""
from setuptools import setup, find_packages

setup(name='quest2keys',
      version='0.1',
      description='transform question to keywords',
      url='https://github.com/ArmandGiraud/quest2keys',
      author='Armand Giraud',
      author_email='armand.giraud.ag@gmail.com',
      license='MIT',
      install_requires=[
          'spacy>2.0.5',
      ],
      tests_require=["pytest"],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      packages=find_packages(),
      
      zip_safe=False)

      