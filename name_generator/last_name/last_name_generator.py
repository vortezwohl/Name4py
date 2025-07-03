from typing_extensions import override

from name_generator.common.base_generator import BaseGenerator


class LastNameGenerator(BaseGenerator):
    def __init__(self):
        super().__init__()

    @override
    def next_name(self):
        ...
