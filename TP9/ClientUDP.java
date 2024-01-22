import java.io.*;
import java.net.*;

public class ClientUDP {
    public static void main(String[] args) {
        try {
            InetAddress addr = InetAddress.getLocalHost();
            System.out.println("Address=" + addr.getHostName());

            String message = "Hello World";
            byte[] data = message.getBytes();
            DatagramPacket sendPacket = new DatagramPacket(data, data.length, addr, 1234);

            DatagramSocket sock = new DatagramSocket();
            sock.send(sendPacket);

            // Attente de la réponse du serveur
            DatagramPacket receivePacket = new DatagramPacket(new byte[1024], 1024);
            sock.receive(receivePacket);

            // Affichage de la réponse du serveur
            String response = new String(receivePacket.getData(), 0, receivePacket.getLength());
            System.out.println("Server response: " + response);

            sock.close();
        } catch (Exception ex) {
            System.out.println("Error!");
            ex.printStackTrace();
        }
    }
}
