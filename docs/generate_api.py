import os
from pathlib import Path

cwd = Path(os.getcwd())
parent = cwd.parent
path_pycatia = Path(parent, 'pycatia')

files = path_pycatia.rglob('*.py')

api_text = 'API\n' \
           '===\n\n'
last_parent = None
body = ''

files = [file for file in files]
files.sort()

api_dict = {}

for file in files:
    parent_directory = file.parents[0].stem

    if parent_directory not in api_dict:
        api_dict[parent_directory] = []

    file_name = file.stem

    if "__init__" not in file_name:
        api_dict[parent_directory].append(file_name)

# write api_index
with open('api_index.rst', 'w') as file:
    header = "API INDEX\n" \
             "=========\n\n\n" \
             ".. toctree::\n" \
             "    :maxdepth: 2\n" \
             "    :caption: Contents:\n\n"

    lines = ""
    for api in api_dict:
        lines = lines + f"    api_{api}\n"

    file.write(header + lines)

for api in api_dict:
    module_file_name = f'api_{api}.rst'

    if module_file_name == 'api_pycatia.rst':
        continue

    header = f"{api}\n" \
             f"{'=' * len(api)}\n\n" \
             f".. highlight:: console\n\n\n"
    with open(module_file_name, 'w') as file:
        file.write(header)

    with open(module_file_name, 'a') as file:
        for module in api_dict[api]:
            content = f".. _{api}-{module}:\n\n" \
                      f"{module}\n" \
                      f"{'-' * len(module)}\n\n" \
                      f".. automodule:: pycatia.{api}.{module}\n" \
                      f"    :members:\n\n\n"
            file.write(content)
