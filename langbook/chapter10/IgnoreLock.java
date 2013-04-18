public class IgnoreLock extends Thread{
    int action_type;
    static int value;
    public static void main(String[] args){
        new IgnoreLock(1).start();
        new IgnoreLock(2).start();
    }

    public IgnoreLock(int action_type){
        this.action_type = action_type;
    }

    public void run() {
        if(action_type == 1){
            for(int i = 0; i < 100; i++){
                consistency_check();
            }
        }else if(action_type == 2){
            for(int i = 0; i < 100; i++){
                ignore_lock();
            }
        }

    }

    static synchronized void consistency_check(){
        value++;
        int old_value = value;
        System.out.println("consistency check start: " + value);
        try{
            sleep(5);
        }catch(InterruptedException e){
            System.exit(1);
        }
        System.out.println("consistency check finished: " + (old_value == value));
    }

    static void ignore_lock(){
        value++;
        try{
            sleep(3);
        }catch(InterruptedException e){
            System.exit(1);
        }
        System.out.println("ignore_lock: " + value);
    }
}

