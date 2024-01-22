import java.io.*;
import java.net.*;

public class ClientTCP3 {
    public static void main(String[] args) {
        try {
            if (args.length == 0) {
                System.out.println("Veuillez fournir la chaîne à envoyer en argument.");
                return;
            }

            Socket socket = new Socket("localhost", 2016);
            DataOutputStream dOut = new DataOutputStream(socket.getOutputStream());
            dOut.writeUTF(args[0]);


            DataInputStream dIn = new DataInputStream(socket.getInputStream());
            String reversedMessage = dIn.readUTF();
            System.out.println("Réponse du serveur : " + reversedMessage);

            dIn.close();
            dOut.close();
            socket.close();
        } catch (Exception ex) {
            System.out.println("Erreur !");
            ex.printStackTrace();
        }
    }
}
