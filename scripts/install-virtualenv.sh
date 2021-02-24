#! /bin/bash

VIRTUALENV_PATH=virtualenv
REQUIREMENTS=requirements.txt
PYTHON=python3

rm -rf "${VIRTUALENV_PATH}"
virtualenv -p "${PYTHON}" "${VIRTUALENV_PATH}"
"${VIRTUALENV_PATH}/bin/pip" install -U pip setuptools
"${VIRTUALENV_PATH}/bin/pip" install -r "${REQUIREMENTS}"
