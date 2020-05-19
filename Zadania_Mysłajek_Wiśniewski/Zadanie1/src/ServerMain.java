import javax.net.ssl.SSLServerSocketFactory;
import java.io.IOException;
import java.net.ServerSocket;
import java.nio.file.LinkOption;
import java.nio.file.Path;
import java.nio.file.Paths;

public class ServerMain {

    private int port;
    private Server server;

    public ServerMain(int port) {
        this.port = port;
        server = new Server(port);
    }

    public static void main(String[] args){
        System.setProperty("javax.net.ssl.keyStore", "src\\keystore\\examplestore1");
        System.setProperty("javax.net.ssl.keyStorePassword", "password");
        int port;
        port = 2020;
        new ServerMain(port);
    }
}