import java.util.Iterator;
import java.util.List;
import java.util.Arrays;

class ForLoopTest{
    public static void main(String[] args){
        int[] items = new int[]{1, 2, 3, 4, 5};

        System.out.println("C style for-loop");
        for(int i = 0; i < items.length; i++){
            int item = items[i];
            System.out.println(item);
        }

        System.out.println("Iterator for-loop");
        List<Integer> items2 = Arrays.asList(new Integer[]{1, 2, 3, 4, 5});
        for (Iterator<Integer> i = items2.iterator(); i.hasNext(); ){
            int item = i.next();
            System.out.println(item);
        }

        System.out.println("For-each loop");
        // http://docs.oracle.com/javase/1.5.0/docs/guide/language/foreach.html
        for(int item: items){
            System.out.println(item);
        }
    }
}