#!/bin/bash
# Restores the given database.
# Usage: pg-restore.sh ~/backups/postgres/pgdump-20130212220733
source $HOME/bin/script-settings-matchmaker.sh

pg_restore -O -c -U $DBUSER -d $DBNAME $1
exit 0
