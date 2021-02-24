run:
	sh ./scripts/run.sh

install:
	sh ./scripts/install-virtualenv.sh
	sh ./scripts/createdb.sh

shell:
	sh ./scripts/shell.sh

createdb:
	sh ./scripts/createdb.sh

test:
	sh ./scripts/test.sh

clean:
	sh ./scripts/cleanall.sh

