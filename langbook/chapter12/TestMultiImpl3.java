public class TestMultiImpl3 extends Foo, Bar {
    public static void main(String[] args){
    }

    // 'public void hello()' is not implemented
}

class Foo {
    public void hello();
}

class Bar {
    public void hello();
}