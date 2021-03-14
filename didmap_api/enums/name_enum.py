from enum import Enum

class NameEnum(Enum):
    # Validate against name and not value.
    # This code comes from this github issue:
    # https://github.com/samuelcolvin/pydantic/issues/598#issuecomment-503032706
    @classmethod
    def __get_validators__(cls):
        cls.lookup = {v: k.value for v, k in cls.__members__.items()}
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return cls.lookup[v]
        except KeyError:
            raise ValueError(f'Invalid value. Please use any of these terms: {", ".join(cls.__members__.keys())}')
    
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update({
            "enum": [k for k, v in cls.__members__.items()]
        })
