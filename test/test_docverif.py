from beancount.loader import load_file
from glob import glob
from os import path
import beancount_docverif
import pytest


def test_basic_import():
    assert(beancount_docverif.docverif)


prefix = path.dirname(__file__)


def test_beancount_import():
    testfile = f'{prefix}/import.beancount'
    base = path.basename(testfile)
    entries, errors, options = load_file(testfile)
    if errors:
        raise RuntimeError(f'{base}: import errors:\n'
                           f'{chr(10).join(e.message for e in errors)}')
    print(f'{base}: ok')


PASS = glob(f'{prefix}/ok_*.beancount')
FAIL = glob(f'{prefix}/fail_*.beancount')


def test_cases_found():
    assert(len(PASS) and len(FAIL))


@pytest.mark.parametrize('testfile', PASS)
def test_pass_examples(testfile):
    base = path.basename(testfile)
    entries, errors, options = load_file(testfile)
    if errors:
        raise RuntimeError(f'{base}: import errors:\n'
                           f'{chr(10).join(e.message for e in errors)}')
    print(f'{base}: ok')


@pytest.mark.parametrize('testfile', FAIL)
def test_fail_examples(testfile):
    base = path.basename(testfile)
    entries, errors, options = load_file(testfile)
    if not errors:
        raise RuntimeError(f'{base}: expected fail but got a pass.')
    print(f'{base}: ok')
