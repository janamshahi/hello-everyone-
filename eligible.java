
import java.util.Scanner;

public class eligible {
    public static void main(String[] args) {
        int x;
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the age of person");
        x=sc.nextInt();
        if(x>=21)  {
            System.out.println("the person is eligible for marrage");
        }
            else{ 
            System.out.println("the person is not eligible for marrage");
        }
    }
}
