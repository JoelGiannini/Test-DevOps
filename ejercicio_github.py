#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:08:29 2022

@author: joelgiannini

Se realizaron los dos ejercicios en uno.

Se realizo con el siguiente usuario de girhub nginxinc y el repositorio ansible-role-nginx.
El cvs se deja en /tmp/github.csv'

"""

from unicodedata import name
import requests
from pprint import pprint
import numpy as np

# Nombre de usuario y variables de Github
username = "nginxinc"
example_repo = "ansible-role-nginx"
repos_list = ['Repositories Name']
commits_list = ['Sha of the commits']
tags_list = ['Tags of the repository']

# Url para request
repos_url = f"https://api.github.com/users/{username}/repos"
tags_url = f"https://api.github.com/repos/{username}/{example_repo}/tags"
commits_url = f"https://api.github.com/repos/{username}/{example_repo}/commits"

# Enviar solicitud de obtención
repo_response = requests.get(repos_url)
tags_response = requests.get(tags_url)
commits_response = requests.get(commits_url)

# # Obtener los datos json
repo_data = repo_response.json()
tags_data = tags_response.json()
commits_data = commits_response.json()

# Obtener repositorios del usuario.
for repository in repo_data:
    repos_list.append(repository["name"])

# Obtener las etiquetas de un repositorio
for tags in tags_data:
    tags_list.append(tags["name"])


# Obtener los commits de un repositorio
for commits in commits_data:
    commits_list.append(commits["sha"])    

# Guardar los datos en un csv
np.savetxt('/tmp/github.csv', [p for p in zip(repos_list, commits_list, tags_list)], delimiter=',', fmt='%s')
