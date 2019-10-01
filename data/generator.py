def generate(file, template, entity):
    #if  

def replace()
    text.replace("$$capital_entity_name$$",  entity[0].upper() + entity[1:] if len(entity) > 0 else entity)\
    .replace("$$entity_semantic_name$$",semanticEntity)\
    .replace("$$entity_name$$",entity[0].lower() + entity[1:] if len(entity) > 0 else entity)\
    .replace("$$column$$",column)\
    .replace("$$referenced_column_name$$",referencedColumnName)\
    .replace("$$id_annotation$$",idAnnotation)\
    .replace("$$cardinality_annotation$$",cardinalityAnnotation)\
    .replace("$$colunm_annotation$$",colunmAnnotation)\
    .replace("$$type$$", type[0].upper() + type[1:] if len(type) > 0 else type)\
    .replace("$$attribute$$",attribute[0].lower() + attribute[1:] if len(attribute) > 0 else attribute)\
    .replace("$$table_name$$", table)\
    .replace("$$domain_attributes$$", domainAttribute)\
    .replace("$$project_name$$",configuration.project["name"])