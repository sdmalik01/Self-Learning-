
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


