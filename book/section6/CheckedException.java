class CheckedException {
    // foo will throw MyException
    void foo() throws MyException{
        throw new MyException();
    }
    // to use foo, declare 'throws MyException' or
    void bar() throws MyException{
        foo();
    }
    // catch MyException
    void baz(){
        try{
            foo();
        }catch(MyException e){
        }
    }
}


class MyException extends Exception {}