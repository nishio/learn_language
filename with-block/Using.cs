using System;

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

class Program
{
    static void Main()
    {
        try
        {
            Console.WriteLine("* sample of normal process");
            process(false);
            Console.WriteLine("\n* sample of failed process");
            process(true);
        }
        catch (ApplicationException e)
        {
            Console.WriteLine("caught: " + e.Message);
        }
        finally
        {
            Console.WriteLine("finally");
        }
    }

    static void process(bool to_fail)
    {
        using (
            MyClass c1 = new MyClass("first"),
                    c2 = new MyClass("second"))
        {
            Console.WriteLine("process");

            if (to_fail)
            {
                Console.WriteLine("failed");
                throw new ApplicationException();
            }
        }
        Console.WriteLine("finished");
    }
}

class MyClass : IDisposable
{
    string name;

    public MyClass(String _name)
    {
        this.name = _name;
        Console.WriteLine("open: " + name);
    }

    void Dispose()
    {
        Console.WriteLine("close: " + name);
    }
}
