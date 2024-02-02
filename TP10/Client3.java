import java.io.BufferedReader;
import java.io.InputStreamReader;
import javax.json.Json;
import javax.json.JsonArray;
import javax.json.JsonObject;
import javax.json.JsonReader;
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;

public class Client3 {
    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
            while (true) {
                System.out.println("Entrez le titre du film (ou 'exit' pour quitter) : ");
                String movieTitle = reader.readLine();

                if ("exit".equalsIgnoreCase(movieTitle)) {
                    System.out.println("Programme terminé.");
                    break;
                }

                String apiKey = "751ea6aa";
                String apiUrl = "http://www.omdbapi.com/?apikey=" + apiKey + "&t=" + movieTitle;

                try (CloseableHttpClient client = HttpClients.createDefault()) {
                    HttpGet request = new HttpGet(apiUrl);
                    System.out.println("Executing request " + request.getRequestLine());

                    try (org.apache.http.client.methods.CloseableHttpResponse resp = client.execute(request)) {
                        System.out.println("Response Line: " + resp.getStatusLine());
                        System.out.println("Response Code: " + resp.getStatusLine().getStatusCode());

                        HttpEntity entity = resp.getEntity();
                        if (entity != null) {
                            InputStreamReader isr = new InputStreamReader(entity.getContent());
                            JsonReader jsonReader = Json.createReader(isr);

                            JsonObject jsonObject = jsonReader.readObject();
                            jsonReader.close();

                            if (jsonObject.getString("Response").equalsIgnoreCase("True")) {
                                // Le film a été trouvé
                                System.out.println("Titre : " + jsonObject.getString("Title"));
                                System.out.println("Date de sortie : " + jsonObject.getString("Released"));
                                System.out.println("Acteurs principaux : " + jsonObject.getString("Actors"));

                                // Récupération du tableau JSON "ratings"
                                JsonArray ratingsArray = jsonObject.getJsonArray("Ratings");

                                // Parcours du tableau pour trouver le score de "Rotten Tomatoes"
                                String rottenTomatoesScore = "N/A";
                                for (int i = 0; i < ratingsArray.size(); i++) {
                                    JsonObject rating = ratingsArray.getJsonObject(i);
                                    if ("Rotten Tomatoes".equalsIgnoreCase(rating.getString("Source"))) {
                                        rottenTomatoesScore = rating.getString("Value");
                                        break;
                                    }
                                }

                                // Affichage du score de "Rotten Tomatoes"
                                System.out.println("Score Rotten Tomatoes : " + rottenTomatoesScore);
                            } else {
                                // Le film n'a pas été trouvé
                                System.out.println("Film non trouvé. Erreur : " + jsonObject.getString("Error"));
                            }
                        }
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
