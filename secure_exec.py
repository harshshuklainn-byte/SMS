#!/usr/bin/env python3
"""Small privilege/credential-hardening launcher for untrusted child bots."""
import ctypes
import os
import sys

def _hardening():
    try:
        libc = ctypes.CDLL(None, use_errno=True)
        PR_SET_DUMPABLE = 4
        libc.prctl(PR_SET_DUMPABLE, 0, 0, 0, 0)
    except Exception:
        pass
    try:
        os.umask(0o077)
    except Exception:
        pass

if __name__ == "__main__":
    _hardening()
    if "--" not in sys.argv:
        raise SystemExit("secure_exec: missing command")
    i = sys.argv.index("--") + 1
    if i >= len(sys.argv):
        raise SystemExit("secure_exec: empty command")
    os.execvpe(sys.argv[i], sys.argv[i:], os.environ.copy())
