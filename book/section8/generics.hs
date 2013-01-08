data Person a = MakePerson {age :: Int, name :: String, something :: a}

x :: Person Int
x = MakePerson {age = 31, name = "nishio", something = 1}

y :: Person String
y = MakePerson {age = 31, name = "nishio", something = "hoge"}

main = do
  print $ something x   -- -> 1
  print $ something y   -- -> "hoge"

  