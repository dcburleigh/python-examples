REPOROOT = /data/git
ETC = /data/etc

-include makefile.conf

REPO = $(REPOROOT)/python-examples

FILES = makefile requirements.txt

CONFIGFILES = example.env ex1.log.yml ex2.log.yml ex3.log.ini ex4.log.ini ex5.log.yml email.example.ini

ETCFILES = deldev_db.cfg deldev_db_creds.py

SCRIPTS = args.py post.py show_config.py log.py list.py log1.py mail.py base.py regex.py db.py dbsa.py j.py jw.py file.py dt.py cli.py wxt.py

UTILS = logger.py

DIRS = templates data db_tables sample utils

$(DIRS): %: $(REPO)/%
	rsync -av $(REPO)/$@/ $@/

util-files:
	rsync -av $(REPO)/utils/ utils/

ITARGETS = $(patsubst %,install-%,$(DIRS))

install-all: $(ITARGETS)

$(ITARGETS): install-%: %
	rsync -av $(REPO)/$</ $</


$(ETCFILES): %: $(ETC)/%
	cp $< $@


$(SCRIPTS): %: $(REPO)/scripts/%
	cp $< $@

$(CONFIGFILES): %: $(REPO)/config/%
	cp $< $@

$(FILES): %: $(REPO)/%
	cp $< $@

install-common: requirements.txt
	pip install -r requirements.txt

install: util-files $(FILES) sample

update-files: $(SCRIPTS)  $(CONFIGFILES)

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

db2: install dbsa.py deldev_db_creds.py install-db_tables
	python dbsa.py

re1: install regex.py
	python regex.py

j1: install j.py
	python j.py

j2: install jw.py templates
	python jw.py

f1: install file.py data
	python file.py

dt1: install dt.py
	python dt.py

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

log6: sample
	python sample/log_simple.py
	ls -l test.log

log-yaml1: install log1.py  ex1.log.yml
	LOG_CONFIG=ex1.log.yml python log1.py
	ls -l test.log

log-yaml2: install log1.py  ex2.log.yml
	LOG_CONFIG=ex2.log.yml python log1.py
	ls -l test.log err.log

log-yaml5: install log1.py  ex5.log.yml
	LOG_CONFIG=ex5.log.yml python log1.py
	ls -l test.log err.log

list1: install list.py
	python list.py

cli1: cli.py
	python cli.py --help
	python cli.py -a --list
	python cli.py -b "do stuff" --name "john doe" --show

post1: post.py post.cnf
	python post.py

wxt1: wxt.py .env
	python wxt.py
