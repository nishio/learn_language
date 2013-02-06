squeak := OSProcess thisOSProcess.

print := [:value |
    squeak stdOut
        nextPutAll: (value asString);
        nextPut: Character lf;
        flush].



Trait named: #MyTrait
    uses: {}
    category: #MyCategory.

MyTrait compile: '
hoge
    ^''T#hoge''
'.

Object subclass: #MyClass
    uses: MyTrait
    instanceVariableNames: ''
    classVariableNames: ''
    poolDictionaries: ''
    category: 'MyCategory'.

print value: (MyClass new hoge).



squeak sigkill: squeak.
