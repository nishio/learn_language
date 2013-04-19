import System.IO.Unsafe

foo x = unsafePerformIO $ do
          print "foo"
          return (x + 1)

bar x = unsafePerformIO $ do
          print "bar"
          return (x * 2)

main = print $ foo(bar(1))