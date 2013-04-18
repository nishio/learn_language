public class TestMultiImpl2 implements Foo, Bar {
    public static void main(String[] args){
    }

    // 'public void hello()' is not implemented
}

interface Foo {
    public void hello();
}

interface Bar {
    public void hello();
}