import java.io.*;
import java.net.*;

public class Clienthttp 
{
    public static void main(String[] args) 
	{
        try 
		{
		
		if (args.length < 1) 
			{
			System.out.println("Veuillez fournir le nom d'hôte en argument.");
			return;
			}

		
		Socket socket = new Socket(args[0], 80);

		
		OutputStreamWriter osw = new OutputStreamWriter(socket.getOutputStream());
		InputStreamReader isw = new InputStreamReader(socket.getInputStream());
		BufferedWriter bufOut = new BufferedWriter(osw);
		BufferedReader bufIn = new BufferedReader(isw);

		
		bufOut.write("GET / HTTP/1.1\r\n");
		bufOut.write("Host: " + args[0] + "\r\n");
		bufOut.write("\r\n");
		bufOut.flush();

		
		String line = bufIn.readLine();
		while (line != null) 
			{
			System.out.println(line);
			line = bufIn.readLine();
			}
		
		bufIn.close();
		bufOut.close();
		socket.close();
		}
		catch (Exception ex) 
		{
			System.out.println("Erreur !");
			ex.printStackTrace();
		}
	}
}
