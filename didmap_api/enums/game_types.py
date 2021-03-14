from .name_enum import NameEnum

class GameTypes(str, NameEnum):
    where_is = "where is?@en"
    whats_the_name = "what's the name?@en"
    puzzle = "puzzle@en"