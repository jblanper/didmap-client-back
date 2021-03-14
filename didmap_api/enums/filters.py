from enum import Enum

class Filters(str, Enum):
    map_type = "skos:ConceptID",
    continent = "didmap:continent@@@geonames:name",
    country = "didmap:country@@@geonames:name",
    region = "didmap:region@@@geonames:name",
    game_type = "didmap:type@@@multiLan:textValue",
    language = "dc:language",
    tag = "sioc_t:Tag",
    author = "gnoss:hasautor"