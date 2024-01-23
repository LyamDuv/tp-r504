import java.io.* ;
import org.apache.http.HttpEntity ;
import org.apache.http.client.* ;
import org.apache.http.client.methods.* ;
import org.apache.http.impl.client.* ;

public class Client1 
{
	public static void main(String[] args) 
	{
		if (args.length != 1)
			{
			System.out.println("Usage: java -classpath \".:/home/user/lib/*\" Client1 <server_url>");
			System.exit(1);
			}


		String serverUrl = args[0];

		try
			{
			
			CloseableHttpClient client = HttpClients.createDefault () ;
			String url = " http :// " + args [0];
			HttpGet request = new HttpGet ( url ) ;
			}
		catch (Exception e)
		{
			e.printStackTrace();
		}
	}
}
