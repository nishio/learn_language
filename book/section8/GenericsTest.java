public class GenericsTest {
    public static void main(String[] args) {
        Foo<Integer> x = new Foo<Integer>();
        x.something = 1;
        Foo<String> y = new Foo<String>();
        y.something = "hoge";
        System.out.println(x.something); // -> 1
        System.out.println(y.something); // -> hoge
    }
}

class Foo<T>{
    public Integer age;
    public String name;
    public T something;
}