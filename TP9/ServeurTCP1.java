import java.io.*;
import java.net.*;

public class ServeurTCP1 {
    public static void main(String[] args) {
        try {
            ServerSocket socketserver = new ServerSocket(2016);
            System.out.println("Serveur en attente...");

            // Attente d'une connexion du client
            Socket socket = socketserver.accept();
            System.out.println("Connexion d'un client");

            // Lecture du message envoyé par le client
            DataInputStream dIn = new DataInputStream(socket.getInputStream());
            System.out.println("Message du client : " + dIn.readUTF());

            // Fermeture des flux et du socket
            socket.close();
            socketserver.close();
        } catch (Exception ex) {
            System.out.println("Erreur !");
            ex.printStackTrace();
        }
    }
}
