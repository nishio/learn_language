public class TestDelegate {
    public static void main(String[] args){
        new UseInheritance().useHello();
        new UseDelegate().useHello();
    }
}


class Hello{
    public void hello(){
        System.out.println("hello!");
    }
}

class UseInheritance extends Hello {
    public void useHello(){
        hello();
    }
}

class UseDelegate {
    Hello h = new Hello();
    public void useHello(){
        h.hello();
    }
}

/* output (checked by coderunner)
hello!
hello!
*/