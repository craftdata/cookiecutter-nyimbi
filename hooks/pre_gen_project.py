#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : hooks/pre_gen_project.py
# Date              : 12.12.2018
# Last Modified Date: 12.12.2018
repo_name = '{{ cookiecutter.repo_name }}'

if hasattr(repo_name, 'isidentifier'):
    assert repo_name.isidentifier(), 'Repo Name should be valid Python identifier!'

docker = '{{ cookiecutter.use_docker }}'.lower()

if docker == 'n':
	import sys

	python_major_version = sys.version_info[0]

	if python_major_version == 2:
		sys.stdout.write("WARNING: nyimbi-Cookiecutter does not support Python 2! Stability is guaranteed with Python 3.4+ only. Are you sure you want to proceed? (y/n)")

		yes_options = set(['y'])
		no_options = set(['n', ''])
		choice = raw_input().lower()
		if choice in no_options:
			sys.exit(1)
		elif choice in yes_options:
			pass
		else:
			sys.stdout.write("Please respond with %s or %s"
				% (', '.join([o for o in yes_options if not o == ''])
					, ', '.join([o for o in no_options if not o == ''])))
