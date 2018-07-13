REPOROOT = /data/git

-include makefile.conf

REPO = $(REPOROOT)/python-examples

FILES = makefile

CONFIGFILES = ex1.log.yml ex2.log.yml ex3.log.ini ex4.log.ini

SCRIPTS = log.py

UTILS = logger.py

DIRS = utils

$(DIRS):
	mkdir -p $@

$(SCRIPTS): %: $(REPO)/scripts/%
	cp $< $@

$(CONFIGFILES): %: $(REPO)/config/%
	cp $< $@

$(FILES): %: $(REPO)/%
	cp $< $@

install-utils:  utils
	rsync -a $(REPO)/utils/ utils/

install: install-utils $(FILES)

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
