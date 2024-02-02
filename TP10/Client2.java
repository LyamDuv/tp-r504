import java.io.*;
import javax.json.*;

import org.apache.http.HttpEntity;
import org.apache.http.client.*;
import org.apache.http.client.methods.*;
import org.apache.http.impl.client.*;

public class Client2 {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java -classpath \".:/home/user/lib/*\" Client2 <server_url>");
            System.exit(1);
        }

        String serverUrl = args[0];

        try {
            CloseableHttpClient client = HttpClients.createDefault();
            String url = "https://" + serverUrl;
            HttpGet request = new HttpGet(url);

            System.out.println("Executing request " + request.getRequestLine());
            CloseableHttpResponse resp = client.execute(request);

            try {
                System.out.println("Response Line: " + resp.getStatusLine());
                System.out.println("Response Code: " + resp.getStatusLine().getStatusCode());

                // Récupération du contenu de la réponse
                HttpEntity entity = resp.getEntity();
                if (entity != null) {
                    InputStreamReader isr = new InputStreamReader(entity.getContent());

                    // Création du lecteur JSON et de l'objet JSON
                    JsonReader reader = Json.createReader(isr);
                    JsonObject jsonObject = reader.readObject();

                    // Fermeture du lecteur JSON et du flux
                    reader.close();
                    isr.close();

                    // Affichage du contenu de l'objet JSON
                    System.out.println("Response JSON Content: ");
                    System.out.println(jsonObject.toString());

                    // Accès à la valeur du champ "Runtime"
                    String runtime = jsonObject.getString("Runtime");
                    System.out.println("Runtime: " + runtime);
                }
            } finally {
                resp.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
