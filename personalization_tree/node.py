import importlib.util as imp
from typing import List, Dict, Callable
from uuid import UUID
import os


class PersonalizationNode:

    allowed_clients = []

    def __init__(self, client: UUID, path: str = __file__) -> None:

        self.allowed = self.has_permission(client)

        if '.py' in path and path[-3:] == '.py':
            path = os.path.dirname(path)

        self.path = path
        self.me = client
        all_nexts = PersonalizationNode.get_all_nexts(path)
        self.nexts = {}

        for next_obj in all_nexts:

            next_path = next_obj['path']
            next_name = next_obj['name']
            next_module = next_obj['module']

            next_instance = next_module(client, next_path)
            if next_instance.allowed:
                self.nexts[next_name] = next_instance

    def func(self, function_name: str, next_name: str = None) -> Callable:
        func = None
        if next_name is not None:
            n = self.nexts[next_name]
            func = getattr(n, function_name)
        else:
            for n in self.nexts.values():
                try:
                    func = getattr(n, function_name)
                    break
                except AttributeError:
                    pass
        if func is not None:
            return func
        raise Exception(f'function not found ({function_name})')

    def get_nexts(self) -> Dict:
        return self.nexts

    def has_permission(self, client: UUID) -> None:

        if client in self.allowed_clients:
            return True
        else:
            return False

    def print_tree(self, level=0) -> None:
        print('-'*level, self.path)
        for n in self.nexts.values():
            n.print_tree(level=level+1)

    @staticmethod
    def get_all_nexts(filepath: str) -> List:
        current_dir = filepath
        files = os.listdir(current_dir)
        directories = []
        for file in files:
            is_dir = os.path.isdir(os.path.join(current_dir, file))
            is_node = 'n_' in file and 'n_' == file[:2]
            if is_dir and is_node:
                directories.append(file)
        target_modules = []
        for directory in directories:
            full_path = os.path.join(current_dir, directory, '__init__.py')
            spec = imp.spec_from_file_location('', full_path)
            modules = imp.module_from_spec(spec)
            spec.loader.exec_module(modules)
            modules_list = dir(modules)
            target_module_name = False
            for module_name in modules_list:
                is_node = 'Node' in module_name and 'Node' == module_name[:4]
                if is_node:
                    target_module_name = module_name
                    break
            if target_module_name:
                target_modules.append(
                    {
                        'path': full_path,
                        'name': target_module_name,
                        'module': getattr(modules, target_module_name)
                    }
                )
        return target_modules
