class MyClass {
    static void my_static_method(){
        System.out.println("I'm static method!");
    }
    void my_instance_method(){
        System.out.println("I'm instance method!");
    }

    public static void main(String[] args){
        MyClass.my_static_method();
        // -> I'm static method!

        MyClass x = new MyClass();
        x.my_instance_method();
        // -> I'm instance method!
    }
};

