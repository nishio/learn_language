PREFIX_CODE = """
squeak := OSProcess thisOSProcess.

print := [:value |
    squeak stdOut
        nextPutAll: (value asString);
        nextPut: Character lf;
        flush].

printException := [:e |
    squeak stdOut
        nextPutAll: (e asString);
        nextPut: Character lf;
        flush].

"""

SUFFIX_CODE = """
squeak sigkill: squeak.
"""

PREFIX_CODE_CATCH_ERROR = PREFIX_CODE + """
[
"""

SUFFIX_CODE_CATCH_ERROR = """
] on: Exception
  do: printException.
""" + SUFFIX_CODE

