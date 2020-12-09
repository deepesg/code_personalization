from uuid import UUID

from personalization_tree.node import PersonalizationNode


class NodeProtheus(PersonalizationNode):

    allowed_clients = ['be9cda0e-e919-4fa0-9f27-2cf582311612']

    def __init__(self, client: UUID, path: str) -> None:
        super().__init__(client, __file__)

    def run(self):
        print('protheus run called!')
