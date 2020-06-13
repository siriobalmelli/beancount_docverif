# Beancount Docverif

Is the "Document Verification" plugin for [beancount][],
fulfilling the following functions:

1. Require that every transaction touching an account have an accompanying
document on disk:

        2000-01-01	open	Income:Job BEAN
          document: "required"

1. Explictly declare the name of a document accompanying a transaction:

        2020-06-01	*	"ABC corp"	"salary"
          document: "2020-06-01.ABC corp - salary.pdf"
          Assets:Bank
          Income:Job -1000 BEAN

1. Explicitly declare that a transaction is expected not to have
an accompanying document:

        2020-06-01	*	"store"	"groceries"
          document: "None"
          Expenses:General
          Assets:Bank -10 BEAN

1. Guarantee integrity: verify that every document declared:
    - does in fact exist on disk
    - is not zero-sized

[beancount]: http://furius.ca/beancount/
