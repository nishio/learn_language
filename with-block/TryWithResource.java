/* output (checked by coderunner)
* sample of normal process
open: first
open: second
process
close: second
close: first
finally

* sample of failed process
open: first
open: second
process
failed
close: second
close: first
catch:java.lang.RuntimeException
finally
*/

public class TryWithResource {

    public static void main(String[] args) {
        System.out.println("* sample of normal process");
        process(false);
        System.out.println("\n* sample of failed process");
        process(true);
    }

    static void process(boolean to_fail){
        try (
             AutoCloseable imp1 = new AutoCloseableImpl("first");
             AutoCloseable imp2 = new AutoCloseableImpl("second")) {
                System.out.println("process");
                if(to_fail){
                    System.out.println("failed");
                    throw new RuntimeException();
                }
        } catch (Exception e) {
            System.out.println("catch:" + e);
        } finally {
            System.out.println("finally");
        }
    }
}

class AutoCloseableImpl implements AutoCloseable {
    String name;
    public AutoCloseableImpl(String name_) {
        this.name = name_;
        System.out.println("open: " + name);
    }

    @Override
    public void close() throws Exception {
        System.out.println("close: " + name);
    }
}