public class TestMultiImpl implements Foo, Bar {
    public static void main(String[] args){
    }

    public void hello(){
        System.out.println("hello!");
    }
}

interface Foo {
    public void hello();
}

interface Bar {
    public void hello();
}