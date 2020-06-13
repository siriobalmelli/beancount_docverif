#!/usr/bin/env bash

LOG=test_log
date >$LOG

RET=0
fail()
{
	echo "FAIL: $*" >&2
	((RET=RET+1))
	return "$RET"
}

run()
{
	{
		echo "$1"
		./docverif.py "$1"
		RR=$?
		echo
	} >>$LOG 2>&1
	return $RR
}

for t in test_ok*.beancount; do
	if run "$t"; then
		echo "OK: $t"
	else
		fail "$t"
	fi
done

for t in test_fail*.beancount; do
	if ! run "$t"; then
		echo "OK: $t"
	else
		fail "$t"
	fi
done

exit "$RET"
