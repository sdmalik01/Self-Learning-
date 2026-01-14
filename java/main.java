
class Demo{
	public static void main(String[] args)
	{
		// This program shows the working demo code of java to print simple information:
		
		System.out.println("					");
		System.out.println("---------------   BIO-DATA  ---------------");
		String Name = "Sayyad Malik";
		int age = 21;
		String email = "sdmalikwork01@gmail.com";
		long number = 9665415026L;
		String Add = "Times Colony";
		float cgpa = 9.3f;
		
		// String formatting using place holders for different types of data variables
	    String result = String.format("My name is %s & I am %d Years old\nYou can contact me on email: %s & Mobile: %d",Name,age,email,number);
		System.out.println(result);
		
		
		// This program demostrate the use of command line arguments:
		
		if (args.length > 0)
		{
			System.out.println("The command line arguments are: ");
			// Iterating the args array using for each loop
			for (String val : args)
				System.out.println(val);
		}
		else
		{
			System.out.println("No command line arguments found.");
		}
	}
}


/*
Java code to perform practical 3: 
1. Finding the minimum and maximum value in the array
2. Count even numbers present in the array
3. Count the target number count in the array given by the user
*/

import java.util.Scanner;

class ArrayOperations {
    public static void main(String[] args) {
        int[] numbers = {3, 12, 10, 52, 12, 45, 474, 52, 8979, 63};

        System.out.print("The array is: ");
        for (int num : numbers) {
            System.out.print(num + " ");
        }
        System.out.print("\n");

        findsmallestLargest(numbers);
        System.out.print("\n");

        CountEven(numbers);
        System.out.print("\n");

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number to count occurrence: ");
        int targetNumber = scanner.nextInt();

        CountOccurence(numbers, targetNumber);
        scanner.close();
    }

    public static void findsmallestLargest(int[] arr) {
        int min = arr[0];
        int max = arr[0];

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
            if (arr[i] > max) {
                max = arr[i];
            }
        }

        System.out.println("Smallest number in the array is: " + min);
        System.out.println("Largest number in the array is: " + max);
    }

    public static void CountEven(int[] arr) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % 2 == 0) {
                count++;
            }
        }
        System.out.println("Total count of even numbers in the array is: " + count);
    }

    public static void CountOccurence(int[] arr, int target) {
        int count_target = 0;
        for (int num : arr) {
            if (num == target) {
                count_target++;
            }
        }
        System.out.println("The target number count in the array is: " + count_target);
    }
}




