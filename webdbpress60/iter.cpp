// comparison of int* pointer and vector<int>::iterator
#include<iostream>
#include<vector>
using namespace std;

int main(){
  int xs[] = {1, 2, 3};
  int* begin = xs;
  int* end = begin + 3;
  vector<int> ys(begin, end);

  {
    cout << "loop with pointer" << endl;
    int* it;
    for(it = begin; it != end; ++it){
      cout << *it << endl;
    }
  }

  {
    cout << "loop with iterator" << endl;
    vector<int>::iterator it;
    for(it = ys.begin(); it != ys.end(); ++it){
      cout << *it << endl;
    }
  }
}
