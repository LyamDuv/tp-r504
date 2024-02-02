import java.io.*;
import org.apache.http.HttpEntity;
import org.apache.http.client.*;
import org.apache.http.client.methods.*;
import org.apache.http.impl.client.*;

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
            CloseableHttpClient client = HttpClients.createDefault();
            String url = "https://" + serverUrl;
            HttpGet request = new HttpGet(url);

            System.out.println("Executing request " + request.getRequestLine());
            CloseableHttpResponse resp = client.execute(request);

            try 
			{
                System.out.println("Response Line: " + resp.getStatusLine());
                System.out.println("Response Code: " + resp.getStatusLine().getStatusCode());

                // Récupération du contenu de la réponse 
                HttpEntity entity = resp.getEntity();
                if (entity != null) 
				{
                    BufferedReader rd = new BufferedReader(new InputStreamReader(entity.getContent()));
                    StringBuffer result = new StringBuffer();
                    String line;
                    while ((line = rd.readLine()) != null) 
					{
                        result.append(line);
                        result.append("\n"); 
                    }
                    rd.close();

                    // Affichage du contenu de la réponse
                    String page = result.toString();
                    System.out.println("Response Content: ");
                    System.out.println(page);
                }
            } finally 
				{
                resp.close();
	            }
        } catch (Exception e)
			{
            e.printStackTrace();
			}
    }
}
