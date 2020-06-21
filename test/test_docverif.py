from sh import bean_check
from glob import glob
from os import path
import beancount_docverif
import pytest


def test_basic_import():
    assert(beancount_docverif.docverif)


prefix = path.dirname(__file__)
PASS = glob(f'{prefix}/ok_*.beancount')
FAIL = glob(f'{prefix}/fail_*.beancount')


def test_cases_found():
    assert(len(PASS) and len(FAIL))


@pytest.mark.parametrize('testfile', PASS)
def test_pass_examples(testfile):
    base = path.basename(testfile)
    try:
        bean_check(testfile)
    except Exception as e:
        print(f'{base}: expected pass but got a fail:\n{e}')
    else:
        print(f'{base}: ok')


@pytest.mark.parametrize('testfile', FAIL)
def test_fail_examples(testfile):
    base = path.basename(testfile)
    try:
        bean_check(testfile)
    except Exception:
        print(f'{base}: ok')
    else:
        print(f'{base}: expected fail but got a pass.')
        assert(False)
