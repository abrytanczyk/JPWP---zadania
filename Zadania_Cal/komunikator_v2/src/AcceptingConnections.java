import java.io.*;
import java.net.Socket;
import java.net.SocketException;

public class AcceptingConnections extends Thread {
    private Server server;
    private boolean running;

    public AcceptingConnections(Server s) {
        this.setServer(s);
        this.setRunning(true);
    }

    @Override
    public void run() {
        try {
            while (isRunning()) {
                try {

                    //2.1
                    Socket socket = this.server.getS();
                    DataInputStream dis = new DataInputStream(socket.getInputStream());
                    DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
                    ClientHandler cH = new ClientHandler(socket, server.getClientNr(), dis, dos, server);
                    Thread t = new Thread(cH);


                    System.out.println("Accepted new connection");


                    getServer().getClientHandlersHM().put(getServer().getClientNr(), cH); // add this client to active clients list

                    t.start(); //uruchom wątek

                    System.out.println("Client nr.: " + getServer().getClientNr() + " joined server.");
                    getServer().setClientNr(getServer().getClientNr() + 1);
                }catch (SocketException e2){
                    //System.out.println("Server socket closed");
                    setRunning(false);
                }

            }
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Error while accepting connection");
        }

    }

    public Server getServer() {
        return server;
    }

    public void setServer(Server server) {
        this.server = server;
    }

    public boolean isRunning() {
        return running;
    }

    public void setRunning(boolean running) {
        this.running = running;
    }
}

