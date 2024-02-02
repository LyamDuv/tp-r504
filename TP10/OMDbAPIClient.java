import java.io.*;
import java.net.URLEncoder;
import org.apache.http.HttpEntity;
import org.apache.http.client.*;
import org.apache.http.client.methods.*;
import org.apache.http.impl.client.*;

public class OMDbAPIClient {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java -classpath \".:/home/user/lib/*\" OMDbAPIClient <movie_title>");
            System.exit(1);
        }

        String apiKey = "751ea6aa"; 
        String movieTitle = args[0];

        try (CloseableHttpClient client = HttpClients.createDefault()) {
            String apiUrl = "http://www.omdbapi.com/?apikey=" + apiKey + "&t=" + movieTitle ;
            HttpGet request = new HttpGet(apiUrl);

            System.out.println("Executing request " + request.getRequestLine());
            
            try (CloseableHttpResponse resp = client.execute(request)) {
                System.out.println("Response Line: " + resp.getStatusLine());
                System.out.println("Response Code: " + resp.getStatusLine().getStatusCode());

                
                HttpEntity entity = resp.getEntity();
                if (entity != null) {
                    try (BufferedReader rd = new BufferedReader(new InputStreamReader(entity.getContent()))) {
                        StringBuilder result = new StringBuilder();
                        String line;
                        while ((line = rd.readLine()) != null) {
                            result.append(line);
                            result.append("\n"); /
                        }

                        
                        try (PrintWriter writer = new PrintWriter("omdb_response.json")) {
                            writer.println(result.toString());
                            System.out.println("Response Content has been written to omdb_response.json");
                        }
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
