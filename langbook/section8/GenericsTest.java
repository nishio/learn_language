public class GenericsTest {
    public static void main(String[] args) {
        Person<Integer> x = new Person<Integer>();
        x.something = 1;
        Person<String> y = new Person<String>();
        y.something = "hoge";
        System.out.println(x.something); // -> 1
        System.out.println(y.something); // -> hoge
    }
}

class Person<T>{
    public Integer age;
    public String name;
    public T something;
}