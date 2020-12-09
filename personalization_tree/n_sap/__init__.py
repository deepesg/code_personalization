from uuid import UUID

from personalization_tree.node import PersonalizationNode


class NodeSap(PersonalizationNode):

    allowed_clients = [
        '0bbd7d4f-9e59-4019-b126-2cd8be0ad9f6',
        'd0c16761-31e6-4468-94cc-299385127e7f'
    ]

    def __init__(self, client: UUID, path: str) -> None:
        super().__init__(client, __file__)

    def run(self):
        print('initializing sap process')
        self.func('step1')()
        print('making step 2')
        self.func('step3')()
