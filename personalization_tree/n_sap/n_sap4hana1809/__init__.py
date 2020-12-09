from uuid import UUID

from personalization_tree.node import PersonalizationNode


class NodeSap4Hana1809(PersonalizationNode):

    allowed_clients = ['0bbd7d4f-9e59-4019-b126-2cd8be0ad9f6']

    def __init__(self, client: UUID, path: str) -> None:
        super().__init__(client, __file__)

    def step1(self):
        print('making step 1 for the 1809 version!')

    def step3(self):
        print('making step 3 for the 1809 version!')
