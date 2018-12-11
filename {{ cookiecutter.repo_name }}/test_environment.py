#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : {{ cookiecutter.repo_name }}/test_environment.py
# Date              : 11.12.2018
# Last Modified Date: 11.12.2018
# -*- coding: utf-8 -*-
# File              : {{ cookiecutter.repo_name }}/test_environment.py
# Date              : 11.12.2018
# Last Modified Date: 11.12.2018
import sys

REQUIRED_PYTHON = "python3" #"{{ cookiecutter.python_interpreter }}"


def main():
    system_major = sys.version_info.major
    if REQUIRED_PYTHON == "python":
        required_major = 2
    elif REQUIRED_PYTHON == "python3":
        required_major = 3
    else:
        raise ValueError("Unrecognized python interpreter: {}".format(
            REQUIRED_PYTHON))

    if system_major != required_major:
        raise TypeError(
            "This project requires Python {}. Found: Python {}".format(
                required_major, sys.version))
    else:
        print(">>> Development environment passes all tests!")


if __name__ == '__main__':
    main()
