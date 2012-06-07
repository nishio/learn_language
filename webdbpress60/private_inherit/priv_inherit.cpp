class Foo{
};

class Bar : Foo{
public:
  Foo* asFoo(){
    return (Foo*)(this);
  }
};

int main(){
  //Foo x = Bar();
  // error: ‘Foo’ is an inaccessible base of ‘Bar’
  //Foo y = (Foo)Bar();
  // error: ‘Foo’ is an inaccessible base of ‘Bar’
  Foo z = *(Bar().asFoo());
  // OK
}
