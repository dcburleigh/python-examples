REPOROOT = /data/git
ETC = /data/etc

-include makefile.conf

REPO = $(REPOROOT)/python-examples

FILES = makefile requirements.txt

CONFIGFILES = ex1.log.yml ex2.log.yml ex3.log.ini ex4.log.ini ex5.log.yml email.example.ini

ETCFILES = deldev_db.cfg

SCRIPTS = log.py mail.py base.py db.py

UTILS = logger.py

DIRS = utils sample

$(ETCFILES): %: $(ETC)/%
	cp $< $@

$(DIRS):
	mkdir -p $@

$(SCRIPTS): %: $(REPO)/scripts/%
	cp $< $@

$(CONFIGFILES): %: $(REPO)/config/%
	cp $< $@

$(FILES): %: $(REPO)/%
	cp $< $@

install-common: requirements.txt
	pip install -r requirements.txt

install-sample:  sample
	rsync -a $(REPO)/sample/ sample/

install-utils:  utils
	rsync -a $(REPO)/utils/ utils/

install: install-utils $(FILES) install-sample

email1: install email.ini mail.py
	python mail.py

email2: install email.ini mail.py
	python mail.py  $(EMAIL)  "testing2"

base1: install  ex1.log.yml base.py
	python base.py
	ls -l test.log

db1: install ex1.log.yml db.py deldev_db.cfg
	python db.py
	ls -l test.log


log-basic: install log.py
	python log.py basic
	ls -l basic.log

log-code: install log.py
	python log.py code
	ls -l debug.log err.log

log1: install log.py ex1.log.yml
	python log.py ex1.log.yml
	ls -l test.log

log2: install log.py ex2.log.yml
	python log.py ex2.log.yml
	ls -l test.log err.log

log3: install log.py ex3.log.ini
	python log.py ex3.log.ini
	ls -l test.log err.log

log4: install log.py ex4.log.ini
	python log.py ex4.log.ini
	ls -l test.log err.log

log5: install log.py ex5.log.yml
	python log.py ex5.log.yml
	ls -l test.log err.log

log6: install-sample
	python sample/log_simple.py
	ls -l test.log
