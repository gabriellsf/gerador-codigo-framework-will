from .settings.parameters import templateDirectory
import glob

def listaAllTemplates():
    templates = []
    for filename in glob.glob(templateDirectory + "*.txt"):
        templateFile = open(filename, "rt", encoding="utf-8") 
        templates.append((filename, templateFile.read()))
        templateFile.close()
    return templates


if (__name__ == '__main__'):
        #Test module
        print(listaAllTemplates)