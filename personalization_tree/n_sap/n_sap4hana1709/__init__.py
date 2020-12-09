from uuid import UUID

from personalization_tree.node import PersonalizationNode


class NodeSap4Hana1709(PersonalizationNode):

    allowed_clients = ['d0c16761-31e6-4468-94cc-299385127e7f']

    def __init__(self, client: UUID, path: str) -> None:
        super().__init__(client, __file__)

    def step1(self):
        print('making step 1 for the 1709 version!')

    def step3(self):
        print('making step 3 for the 1709 version!')
