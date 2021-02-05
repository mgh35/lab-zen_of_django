set -e

cd "$(dirname "$0")"

VENV=.venv-django

pyenv local 3.9.1
if [ ! -d $VENV ]
then
    python -m venv $VENV
fi
source $VENV/bin/activate

pip install -r requirements.txt

python backend/manage.py migrate
python backend/manage.py runserver
