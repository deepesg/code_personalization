from uuid import UUID

from personalization_tree.node import PersonalizationNode


class NodeOracle(PersonalizationNode):

    allowed_clients = ['d5a23e2b-1400-45f3-92ad-3abb1b60e28e']

    def __init__(self, client: UUID, path: str) -> None:
        super().__init__(client, __file__)

    def run(self):
        print('initializing oracle process')
        print('making step 1')
        print('making step 2')
        print('making step 3')
