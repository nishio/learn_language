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
        nextPutAll: (e messageText);
        nextPut: Character lf;
        flush].

[
"""

SUFFIX_CODE = """
] on: Exception
  do: printException.

squeak sigkill: squeak.
"""
