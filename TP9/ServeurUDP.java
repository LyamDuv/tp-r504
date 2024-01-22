import java.io.*;
import java.net.*;

public class ServeurUDP {
    public static void main(String[] args) {
        try {
            DatagramSocket sock = new DatagramSocket(1234);
            while (true) {
                System.out.println("-Waiting for data");
                DatagramPacket receivePacket = new DatagramPacket(new byte[1024], 1024);
                sock.receive(receivePacket);

               
                String receivedData = new String(receivePacket.getData(), 0, receivePacket.getLength());
                InetAddress clientAddress = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();

                System.out.println("Received data: " + receivedData);

                // Sending the received data back to the client
                String responseMessage = "Server received: " + receivedData;
                byte[] responseData = responseMessage.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(responseData, responseData.length, clientAddress, clientPort);
                sock.send(sendPacket);
            }
        } catch (Exception ex) {
            System.out.println("Error!");
            ex.printStackTrace();
        }
    }
}
