data Foo a = Person {age :: Int, name :: String, something :: a}

x :: Foo Int
x = Person {age = 31, name = "nishio", something = 1}

y :: Foo String
y = Person {age = 31, name = "nishio", something = "hoge"}

main = do
  print $ something x   -- -> 1
  print $ something y   -- -> "hoge"

  