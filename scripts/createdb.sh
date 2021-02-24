#! /bin/sh

env PYTHONPATH="." ./virtualenv/bin/flask db init
env PYTHONPATH="." ./virtualenv/bin/flask db migrate -m "users table"
env PYTHONPATH="." ./virtualenv/bin/flask db upgrade