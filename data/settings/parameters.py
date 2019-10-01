project = {
    "name": "SGO"
}

templateDirectory = "data/templates/"
outputRoot = "result/src/ipp/aci/" + project["name"] + "/"

outputDir = {
    "controller": "visao/",
    "service": "servicos/",
    "data": "dados/",
    "repository": "dados/oracle/",
    "domain": "dominio/",
    
} 
outputName = {
    "controller": "$$capital_entity_name$$Controller",
    "service": "ServicosDe$$capital_entity_name$$",
    "data": "I$$capital_entity_name$$Dados",
    "repository": "Oracle$$capital_entity_name$$Dados",
    "domain": "$$capital_entity_name$$"
}
