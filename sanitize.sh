#!/usr/bin/env bash
# maintainer's personal script; use at own risk
# run inside 'nix-shell --pure'
set -e

# Simplify path handling
pushd "$(dirname "$(realpath "$0")")"
trap "popd" EXIT


# Remove any build or runtime arifacts
# ... python can be a bit noisy with artifacts floating around the project dir
rm -rfv \
	.eggs .tox \
	build dist result \
	"test/test_log"
	beancount_docverif.egg-info \
find . \( -name "__pycache__" -o -name "*.pyc" \) -exec rm -rfv '{}' \; \
	2>/dev/null || true

# if we are just cleaning; exit now
[ "$1" == clean ] && exit 0


# Install dev environment and run tests
# python3 -m pip install -e .[dev]
python3 -m pytest


# Build both binary and source distributions locally
python3 setup.py bdist_wheel sdist

echo "you can now do 'twine upload dist/*'"
