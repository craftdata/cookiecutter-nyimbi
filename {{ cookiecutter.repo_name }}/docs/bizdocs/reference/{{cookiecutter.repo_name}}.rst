{{ cookiecutter.repo_name }}
{{ "=" * cookiecutter.repo_name|length }}

.. testsetup::

    from {{ cookiecutter.repo_name }} import *

.. automodule:: {{ cookiecutter.repo_name }}
    :members:
