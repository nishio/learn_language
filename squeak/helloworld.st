squeak := OSProcess thisOSProcess.

squeak stdOut
    nextPutAll: 'hello world';
    nextPut: Character lf;
    flush.

squeak sigkill: squeak.
