Deployment with Elastic Beanstalk
==========================================

.. index:: Elastic Beanstalk

Warning: Experimental
---------------------

This is experimental. For the time being there will be bugs and issues. If you've never used Elastic Beanstalk before, please hold off before trying this option.

On the other hand, we need help cleaning this up. If you do have knowledge of Elastic Beanstalk, we would appreciate the help. :)

Prerequisites
-------------

* awsebcli

Instructions
-------------

If you haven't done so, create a directory of environments::

  eb init -p python3.4 MY_REPO_NAME

Replace `MY_REPO_NAME` with the value you entered for `repo_name`.

Once that is done, create the environment (server) where the app will run::

  eb create MY_REPO_NAME
  # Note: This will eventually fail on a postgres error, because postgres doesn't exist yet

Now make sure you are in the right environment::

  eb list

If you are not in the right environment, then put yourself in the correct one::

  eb use MY_REPO_NAME

Set the environment variables. Notes:  You will be prompted if the `.env` file is missing. The script will ignore any PostgreSQL values, as RDS uses it's own system::

  # Set the environment variables
  python ebsetenv.py

Speaking of PostgreSQL, go to the Elasting Beanstalk configuration panel for RDS. Create new RDS database, with these attributes:

* PostgreSQL
* Version 9.4.9
* Size db.t2.micro (You can upgrade later)

(Get some coffee, this is going to take a while)

Once you have a database specified, deploy again so your instance can pick up the new PostgreSQL values::

  eb deploy

Take a look::

  eb open

FAQ
-----

Why Not Use Docker on Elastic Beanstalk?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because I didn't want to add an abstraction (Docker) on top of an abstraction (Elastic Beanstalk) on top of an abstraction (Cookiecutter Django).

Why Can't I Use Both Docker/Heroku with Elastic Beanstalk?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because the environment variables that our Docker and Heroku setups use for PostgreSQL access is different then how Amazon RDS handles this access. At this time we're just trying to get things to work reliably with Elastic Beanstalk, and full integration will come later.
