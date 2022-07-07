
.PHONY: test

test:
	EDGEDB_CREDENTIALS_FILE=~/.config/edgedb/credentials/tidskrift.json pytest -s