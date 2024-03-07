python3 -m venv virenv
source ./virenv/bin/activate
cd PeerGrader
pip install -r requirements.txt
python3 manage.py runserver
