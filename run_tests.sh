#!/usr/bin/env bash

LOG=test_log
date >$LOG

RET=0
fail()
{
	echo "FAIL: $*" >&2
	((RET=RET+1))
}

for t in test_ok_*.beancount; do
	bean-check "$t" >>$LOG 2>&1 || fail "$t"
	echo "OK: $t"
done

for t in test_fail_*.beancount; do
	bean-check "$t" >>$LOG 2>&1 && fail "$t"
	echo "OK: $t"
done

exit "$RET"
