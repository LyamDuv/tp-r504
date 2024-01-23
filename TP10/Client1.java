import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;

public class Client1 
{
	public static void main(String[] args) 
	{
		if (args.length != 1)
			{
			System.out.println("Usage: java -classpath \".:~/lib/*\" Client1 <server_url>");
			System.exit(1);
			}

		String serverUrl = args[0];

		try
			{
			// Exemple d'utilisation d'Apache HttpComponents pour envoyer une requête GET
			CloseableHttpClient httpClient = HttpClients.createDefault();
			HttpGet httpGet = new HttpGet(serverUrl);

			HttpResponse response = httpClient.execute(httpGet);

			httpClient.close();
			}
		catch (Exception e)
		{
			e.printStackTrace();
		}
	}
}
