/* output (checked by coderunner)
* sample of normal process
open: first
open: second
process
close: second
close: first
finished

* sample of failed process
open: first
open: second
process
failed
close: second
close: first
caught: An application exception has occurred.
finally
*/
using System;

class Program
{
    static void Main()
    {
        try{
                System.Console.WriteLine("* sample of normal process");
                process(false);
                System.Console.WriteLine("\n* sample of failed process");
                process(true);
        }catch (System.ApplicationException e){
                System.Console.WriteLine("caught: " + e.Message);
        }finally{
                System.Console.WriteLine("finally");
        }
    }

    static void process(bool to_fail){
        using (
              MyClass c1 = new MyClass("first"),
                      c2 = new MyClass("second"))
        {
                System.Console.WriteLine("process");
                if(to_fail){
                        System.Console.WriteLine("failed");
                        throw new System.ApplicationException();
                }
        }
        Console.WriteLine("finished");
    }
}


class MyClass : IDisposable
{
    String name;
    public MyClass(String _name)
    {
        this.name = _name;
        System.Console.WriteLine("open: " + name);
    }

    void IDisposable.Dispose()
    {
        System.Console.WriteLine("close: " + name);
    }
}