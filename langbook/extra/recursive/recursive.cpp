#include <stack>
#include <tuple>
#include <vector>
#include <iostream>
#include <boost/any.hpp>
#include <boost/foreach.hpp>

using boost::any_cast;
typedef std::vector<boost::any> many;


bool is_integer(const boost::any& x){
  return (x.type() == typeid(int));
}


void show_many(const many& xs);

void show_any(const boost::any x){
  if(is_integer(x)){
    std::cout << any_cast<int>(x);
  }else{
    show_many(any_cast<many>(x));
  }
}


void show_many(const many& xs){
  std::cout << "[";
  for(int i = 0; i < xs.size(); i++){
    if(i > 0){
      std::cout << ", ";
    }
    show_any(xs[i]);
  }
  std::cout << "]";
}


int total(const many& xs){
  int result = 0;
  BOOST_FOREACH( const boost::any& x, xs ){
    #ifdef VERBOSE
    std::cout << "xs:";
    show_many(xs);
    std::cout << ", x:";
    show_any(x);
    std::cout << ", result:" << result << std::endl;
    #endif

    if(is_integer(x)){
      result += any_cast<int>(x);
    }else{
      result += total(any_cast<many>(x));
    }
  }
  return result;
}


int total2(const many& xs){
  int i;
  boost::any x;
  int result = 0;

  for(i = 0; i < xs.size(); i++){
    x = xs[i];

    #ifdef VERBOSE
    std::cout << "xs:";
    show_many(xs);
    std::cout << ", x:";
    show_any(x);
    std::cout << ", i:" << i << ", result:" << result << std::endl;
    #endif

    if(is_integer(x)){
      result += any_cast<int>(x);
    }else{
      result += total2(any_cast<many>(x));
    }
  }
  return result;
}

// ローカル変数を保存するためのスタック
typedef std::tuple<many, int, boost::any, int> frame_t;
std::stack<frame_t> stack;

// 返り値を保存するための変数
int function_result;

int total3(many& xs){
 ENTRYPOINT:
  int i;
  boost::any x;
  int result = 0;

  for(i = 0; i < xs.size(); i++){
    x = xs[i];

    #ifdef VERBOSE
    std::cout << "xs:";
    show_many(xs);
    std::cout << ", x:";
    show_any(x);
    std::cout << ", i:" << i << ", result:" << result << std::endl;
    #endif

    if(is_integer(x)){
      result += any_cast<int>(x);
    }else{
      // result += total(any_cast<many>(x))相当のことを実現するために
      // 1: 現在のローカル変数をスタックに保存する
      stack.push(make_tuple(xs, i, x, result));
      // 2: 引数xsを書き換える
      xs = any_cast<many>(x);
      // 3: 関数冒頭へジャンプ
      goto ENTRYPOINT;

    RETURNPOINT: // 6: 呼び出された関数からreturnするとここに戻ってくる
      // 7: スタックに保存しておいた値を復元する
      frame_t f = stack.top();
      stack.pop();
      xs = std::get<0>(f);
      i = std::get<1>(f);
      x = std::get<2>(f);
      result = std::get<3>(f);

      // 8: 関数の返り値を使う
      result += function_result;
    }
  }

  // ループが終わったのでreturn result;に相当することをやる
  if(!stack.empty()){
    // スタックが空でないなら
    // 4: 返り値を決められた場所に保存
    function_result = result;
    // 5: 関数呼び出し直後(上記6)に戻る
    goto RETURNPOINT;
  }
  // スタックが空の時は自前管理の呼び出しではないので本物のreturnをする
  return result;
}


int main(){
  many xs;
  xs.push_back((boost::any) 1);

  many tmp;
  tmp.push_back((boost::any) 2);
  tmp.push_back((boost::any) 3);
  xs.push_back(tmp);

  xs.push_back((boost::any) 4);

  std::cout << total(xs) << std::endl;
  std::cout << total2(xs) << std::endl;
  std::cout << total3(xs) << std::endl;
}
