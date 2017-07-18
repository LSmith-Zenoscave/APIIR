#!/bin/bash
set -e
set -x

if [[ "$(uname -s)" == "Darwin" ]]; then
    sw_vers
    brew update && brew upgrade pyenv
    PYENV_ROOT="$HOME/.pyenv"
    PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"

    case "${TOXENV}" in
        py27)
            curl -O https://bootstrap.pypa.io/get-pip.py
            python get-pip.py --user
            ;;
        pypy3)
            pyenv install pypy3-2.4.0
            pyenv global pypy3-2.4.0
            ;;
        pypy*)
            pyenv install "pypy-$PYPY_VERSION"
            pyenv global "pypy-$PYPY_VERSION"
            ;;
        docs)
            brew install enchant
            curl -O https://bootstrap.pypa.io/get-pip.py
            python get-pip.py --user
            ;;
        *)
            pyenv install ${VERSION}
            pyenv global ${VERSION}
            ;;
    esac

    pyenv rehash
    python -m pip install --user virtualenv coverage
else
    # temporary pyenv installation to get latest pypy until the travis
    # container infra is upgraded

    PYENV_ROOT="$HOME/.travis-pyenv"
    curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
    PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"

    if [[ "${TOXENV}" = pypy3* ]]; then
        pyenv install "pypy3-$PYPY_VERSION"
        pyenv global "pypy3-$PYPY_VERSION"
    elif [[ "${TOXENV}" = pypy* ]]; then
        pyenv install "pypy-$PYPY_VERSION"
        pyenv global "pypy-$PYPY_VERSION"
    elif [[ -n "${VERSION}" ]]; then
        pyenv install "${VERSION}"
        pyenv global "${VERSION}"
    fi

    pyenv rehash
    pip install virtualenv coverage
fi

python -m virtualenv ~/.venv
source ~/.venv/bin/activate
pip install tox codecov