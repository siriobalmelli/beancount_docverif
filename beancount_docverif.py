#!/usr/bin/env python3
"""docverif
Verify that expected documents exist for beancount files.

NOTE that we depend on beancount itself already finding documents,
which requires eg:

    option "documents" "./"

in the beancount file itself.
"""

from beancount.core.data import Document, Open, Transaction
from os import path

# Error reporting done with a custom collection
from collections import namedtuple
DocumentError = namedtuple('DocumentError', 'source message entry')

__plugins__ = ('docverif', )
DEBUG = 0


def txn2doc(entry: Transaction) -> str:
    """
    Returns the "expected" document name for an entry, as a string.
    """
    return f'{entry.date}.{entry.payee} - {entry.narration}.pdf'


def docverif(entries: list, options: list) -> (list, list):
    """
    Beancount already looks on disk and creates Document entries for all files;
    parse those only.

    We specifically look for a document entry if told to do so with
    a "document:" declaration in an entry; throw an error if not found.

    Look for an optional directive in account Open entry:

        document: "Require"

    If found, every transaction involving that account will now error
    in the event a corresponding Document is not found.

    Allow the user to override this behavior by specifying:

        document: "None"

    Returns (entries, errors) as expected of a beancount plugin.
    NOTE that entries is unchanged: this plugin only generates errors.
    """
    # First pass through entries to accumulate:
    # - doc directives:
    docs = set()  # {basename(filename)}
    # - required accounts:
    reqs = set()  # {acct_name}

    err = []
    for ent in entries:
        meta = ent.meta

        if isinstance(ent, Document):
            fname = ent.filename
            # Beancount sometimes lies about (ahem, "corrects") 'filename'
            if not path.exists(fname):
                err.append(DocumentError(meta, f'fake path: "{fname}"', ent))
            else:
                docs.add(path.basename(fname))
        elif isinstance(ent, Open):
            if meta.get('docverif', '') == 'Require':
                reqs.add(ent.account)
    if DEBUG:
        print(f'documents: {docs}')
        print(f'required accounts: {reqs}')

    for ent in entries:
        meta = ent.meta

        # Explicit 'document' entries if specified/required by user,
        # also includes the special 'None' entry meaning "don't bother me"
        fname = meta.get('document')
        if fname:
            if fname != 'None' and fname not in docs:
                err.append(DocumentError(meta, f'missing: "{fname}"', ent))

        # Implicit document entries: all the accounts where the Open statement
        # includes a 'document_required' entry.
        elif isinstance(ent, Transaction):
            if next((p for p in ent.postings if p.account in reqs), None):
                imp = txn2doc(ent)
                if imp not in docs:
                    err.append(DocumentError(meta, f'expected eg: {imp}', ent))

    return entries, err
