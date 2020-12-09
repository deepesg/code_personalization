from personalization_tree.starter import Starter


def main(client):

    starter = Starter(client, __file__)
    starter.print_tree()
    starter.run()


if __name__ == '__main__':
    client = 'd0c16761-31e6-4468-94cc-299385127e7f'
    main(client)

# clients
# client_x  (usa protheus)              be9cda0e-e919-4fa0-9f27-2cf582311612
# client_y  (usa sap)                   0bbd7d4f-9e59-4019-b126-2cd8be0ad9f6
# client_z  (usa oracle)                d5a23e2b-1400-45f3-92ad-3abb1b60e28e
# client_w  (usa sap em outra versao)   d0c16761-31e6-4468-94cc-299385127e7f
