REPOROOT = /data/git

-include makefile.conf

REPO = $(REPOROOT)/python-examples

FILES = makefile

CONFIGFILES = ex1.log.yml ex2.log.yml ex3.log.ini ex4.log.ini ex5.log.yml 

SCRIPTS = log.py

UTILS = logger.py

DIRS = utils sample

$(DIRS):
	mkdir -p $@

$(SCRIPTS): %: $(REPO)/scripts/%
	cp $< $@

$(CONFIGFILES): %: $(REPO)/config/%
	cp $< $@

$(FILES): %: $(REPO)/%
	cp $< $@

install-sample:  sample
	rsync -a $(REPO)/sample/ sample/

install-utils:  utils
	rsync -a $(REPO)/utils/ utils/

install: install-utils $(FILES) install-sample

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
