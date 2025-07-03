from typing_extensions import override

from name_generator.common.base_generator import BaseGenerator
from name_generator.first_name import FIRST_NAMES


class FirstNameGenerator(BaseGenerator):
    def __init__(self):
        super().__init__(names=FIRST_NAMES.get_top_names())

    @override
    def next_name(self):
        ...
