{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

This project presupposes that you are going to use flask-appbuilder and pytorch for the AI component.


Organization of {{cookiecutter.project_name}}
------------
.
├── LICENSE
├── Makefile
├── README.md
├── ai
│   ├── data
│   │   ├── external
│   │   ├── interim
│   │   ├── processed
│   │   └── raw
│   ├── features
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── predict_model.py
│   │   └── train_model.py
│   ├── notebooks
│   ├── reports
│   │   └── figures
│   └── visualization
│       ├── __init__.py
│       └── visualize.py
├── devdocs
│   ├── Makefile
│   ├── commands.rst
│   ├── conf.py
│   ├── getting-started.rst
│   ├── index.rst
│   └── make.bat
├── refs
├── requirements.txt
├── setup.py
├── src
│   ├── __init__.py
│   ├── app
│   │   ├── README.rst
│   │   ├── app
│   │   │   ├── __init__.py
│   │   │   ├── mixins.py
│   │   │   ├── models.py
│   │   │   ├── templates
│   │   │   │   └── 404.html
│   │   │   ├── translations
│   │   │   │   └── pt
│   │   │   │       └── LC_MESSAGES
│   │   │   │           ├── messages.mo
│   │   │   │           └── messages.po
│   │   │   └── views.py
│   │   ├── babel
│   │   │   ├── babel.cfg
│   │   │   └── messages.pot
│   │   ├── config-a.py
│   │   ├── config.py
│   │   ├── gevent_run.py
│   │   └── run.py
│   ├── data
│   │   ├── __init__.py
│   │   └── make_dataset.py
│   ├── db
│   │   ├── gen_script.sh
│   │   ├── gendb.sh
│   │   └── method.txt
│   └── zarc
├── test_environment.py
└── tox.ini
