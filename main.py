import sys
import os
from data import fileReader, fileMaker
from data.settings import entities 

for entitie in entities.data:
    templates = fileReader.listaAllTemplates()
    for template in templates:
        