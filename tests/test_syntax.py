"""Basic sanity tests for the repository.

These tests simply attempt to compile every Python file under ``app/``.  The
objective is to catch syntax errors early in CI without actually running the
pygame-based game logic.
"""

import glob
import os
import py_compile


def test_compile_all_app_files():
    all_py = glob.glob(os.path.join("app", "*.py"))
    assert all_py, "No python files found in app/"
    for path in all_py:
        # py_compile will raise a PyCompileError if the file contains syntax
        # errors.  Imports are not executed, so pygame is not required.
        py_compile.compile(path, doraise=True)
