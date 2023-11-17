"""arquivo main."""

# Para onde vai as instalações dos pacotes quando não tem um ambiente virtual

# Com o venv, o site-packages fica dentro do divetório do projeto

import site
import sys

# print(site.getsitepackages())

for path in sys.path:
    print(path)
