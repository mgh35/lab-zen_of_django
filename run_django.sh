set -e

cd "$(dirname "$0")"

VENV=.venv

pyenv local 3.9.1
if [ ! -d $VENV ]
then
    python -m venv $VENV
fi
source $VENV/bin/activate

pip install -r requirements.txt

cd blog
python manage.py migrate
python manage.py runserver
