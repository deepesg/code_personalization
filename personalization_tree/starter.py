from uuid import UUID

from personalization_tree.node import PersonalizationNode


class Starter(PersonalizationNode):

    def __init__(self, client: UUID, path: str) -> None:
        super().__init__(client, __file__)

    def run(self):
        func = self.func('run')
        func()
