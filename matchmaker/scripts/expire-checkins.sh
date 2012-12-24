#!/bin/bash
source $HOME/bin/script-settings-matchmaker.sh
source $HOME/Envs/$VENV_NAME/bin/activate

$HOME/webapps/$DJANGO_APP_NAME/$PROJECT_NAME/manage.py expire_checkins
