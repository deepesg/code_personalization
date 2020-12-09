from uuid import UUID

from personalization_tree.node import PersonalizationNode


class NodeProtheus(PersonalizationNode):

    allowed_clients = ['be9cda0e-e919-4fa0-9f27-2cf582311612']

    def __init__(self, client: UUID, path: str) -> None:
        super().__init__(client, __file__)

    def run(self):
        print('initializing protheus process')
        print('making step 1')
        print('making step 2')
        print('making step 3')
