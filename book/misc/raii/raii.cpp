#include <cstdio>
#include <stdexcept> // std::runtime_error

bool to_throw_on_open = false;
bool to_throw_on_use = false;

int open(){
  printf("try to open\n");
  if(to_throw_on_open) {
    printf("throw\n");
    throw std::runtime_error("error on open");
  }
  printf("open\n");
  return 0;
}

int close(){
  printf("close\n");
  return 0;
}

int use_resource(){
  printf("try to use\n");
  if(to_throw_on_use) {
    printf("throw\n");
    throw std::runtime_error("error on use");
  }
  printf("use\n");
  return 0;
}

class SampleRAII {
public:
  SampleRAII()
    : resource(open()) {
  }

  ~SampleRAII() {
    close();
  }

  void use() {
    use_resource();
  }

private:
    int resource;
};

int main(){
  printf("scenario1: normal case\n");
  {
    SampleRAII x; // open
    x.use(); // use
  } // close

  printf("\n\nscenario2: failed to open\n");
  to_throw_on_open = true;
  try{
    SampleRAII x; // open
    x.use(); // use
  }catch(std::runtime_error& e){
    printf("exception caught: %s\n", e.what());
  }

  printf("\n\nscenario3: opened, but failed to use\n");
  to_throw_on_open = false;
  to_throw_on_use = true;
  try{
    SampleRAII x; // open
    x.use(); // use
  }catch(std::runtime_error& e){
    printf("exception caught: %s\n", e.what());
  }
}
