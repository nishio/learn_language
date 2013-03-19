test:
	javac Test.java
	java -Xmx1G -XX:PermSize=4m -XX:MaxPermSize=4m -XX:+PrintGCDetails -XX:+UseSerialGC Test

test-without-permsize:
	javac Test.java
	java -Xmx1G -XX:+PrintGCDetails -XX:+UseSerialGC Test
