# venv

Create Python virtual environments

## set up

* install Python(s)

which python
$ ls -l /usr/local/bin/python3

* install virtualenv

pip install virtualenv


$ virtualenv --version
15.1.0


* install venv

cd
mkdir venv

cd venv

* add to your BASH .profile
 topy.sh

## create environment

* select path to path
* select label for this venv
* use that label as the prompt
* clear:

virtualenv -p /path/to/python  --clear --prompt 'ex>' ex

### use

cd /path/to/project

topy ex  

pip install -r requirements.txt
