# Beancount Docverif [![Build Status](https://travis-ci.org/siriobalmelli/beancount_docverif.svg?branch=master)](https://travis-ci.org/siriobalmelli/beancount_docverif)

Docverif is the "Document Verification" plugin for [beancount][],
fulfilling the following functions:

1. Require that every transaction touching an account have an accompanying
document on disk:

    ```beancount
    2000-01-01  open  Expenses:General BEAN
      docverif: "Require"
    ```

1. Explicitly declare the name of a document accompanying a transaction:

    ```beancount
    ; Document entry pointing to a working document: should validate correctly
    2020-06-01  *   "plumber"   "fix faucet leak"
      document: "2020-06-01.plumber - services.pdf"
      Expenses:General
      Assets:Bank -150 BEAN
    ```

1. Explicitly declare that a transaction is expected not to have
an accompanying document:

    ```beancount
    ; Explicit "None" document: should ignore missing document
    2020-06-01  *   "store" "groceries"
      document: "None"
      Expenses:General
      Assets:Bank -10 BEAN
    ```

1. Look for an "implicit" PDF document matching transaction data:

    ```beancount
    ; Document entry without an explicit "document" entry,
    ; should implicitly match document: "2020-06-01.plumber - services.pdf"
    2020-06-01  *   "plumber"   "services"
      Expenses:General
      Assets:Bank -150 BEAN
    ```

1. Associate (and require) a document with any type of entry,
including `open` entries themselves:

    ```beancount
    2000-01-01  open    Assets:Bank BEAN
      docverif: "Require"
      document: "2020-06-01.plumber - services.pdf"
    ```

1. Guarantee integrity: verify that every document declared
does in fact exist on disk.

## Installation

```python
pip install beancount_docverif
```

## Usage

In your toplevel `.beancount` file, include:

```beancount
plugin  "beancount_docverif"
option  "documents" "./"
```

See the `.beancount` files in [test](./test) for examples.

## Developing

Install package and dev requirements locally:

```bash
python3 -m pip install -e .[dev]
```

Run tests:

```bash
python3 -m pytest
```

Build both binary and source distributions locally:

```bash
python3 setup.py bdist_wheel sdist
```

See [sanitize.sh](./sanitize.sh) for maintainer's personal tooling.

## Beancount Quirks

1. We depend on beancount itself finding documents
and auto-generating `Document` entries.
This requires a `documents` option in the beancount file itself, eg:

    ```beancount
    option "documents" "./"
    ```

1. Subdirectory format *TODO*

1. Fictitious *TODO*

1. Filename must be valid (eg. "broken.pdf" is out)

[beancount]: http://furius.ca/beancount/
