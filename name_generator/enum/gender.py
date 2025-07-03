from enum import Enum


class Gender(Enum):
    Male = 'male'
    Female = 'female'

    @property
    def gender_identifier(self):
        return self.value[0].upper()
