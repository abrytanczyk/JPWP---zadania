import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;

public class Server {

    private static final int port = 1488;

    private static ServerSocket serverSocket;
    private static Socket clientSocket;
    private static int i = 0;
    private String site;
    private ArrayList<String> coronavirusSubscribers = new ArrayList<>();
    private Mailer mailer = new Mailer();
    //Type your email and password for testing purposes
    private String email;
    private String emailPassword;

    public ArrayList<String> getCoronavirusSubscribers() {
        return coronavirusSubscribers;
    }

    public void addSubscriber(String newSubscriber){
        //Add new subscriber to list
        coronavirusSubscribers.add(newSubscriber);
        //Send welcome email
        mailer.sendEmail(email, emailPassword, newSubscriber, "Nowa subskrypcja", "Drogi użytkowniku,\n\n" +
                "Otrzymujesz tego maila, gdyż ktoś zarejestrował go do newslettera, dotyczącego najświeższych " +
                "informacji o koronawirusie.\n\nJeśli to nie byłeś ty prosimy o kontakt na adres mailowy: " +
                email);

    }

    public void sendMail(){
        //TODO 3.2 Napisz funkcję, wysyłającą maile do wszystkich sybskrybentów
    }

    Server() throws IOException {
        //Add your email to check correctness of your code
        /*coronavirusSubscribers.add("");
        this.sendMail();*/

        //Start timer to send email every 8h
        timer.start();
        try {
            //Create server socket
            serverSocket = new ServerSocket(port);
        } catch (IOException e) {
            System.err.println("Could not listen on a port: " + port);
        }

        while (true) {
            Socket socket = null;
            try {
                //Accept incoming requests
                // 2.1 Akcpetuj połączenia, przychodzące od klientów
                socket = serverSocket.accept();
                //Create data streams to communicate
                // 2.1 Utórz przychodzący i wychodzący strumień danych, zapisz je jako in oraz out
                DataOutputStream out = new DataOutputStream(socket.getOutputStream());
                DataInputStream in = new DataInputStream(socket.getInputStream());
                //Create new ClientHandler instance and pass to it server, socket and data streams
                ClientHandler handler = new ClientHandler(this, socket, in, out);
            } catch (Exception e) {
                socket.close();
                e.printStackTrace();
            }

        }
    }
    //Create timer to send email every 8h
    private Timer timer = new Timer(28800000, new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) { sendMail(); }
    });

    public static void main(String[] args) {
        try {
            Server server = new Server();
        } catch (IOException e) {
            System.err.println(e);
        }
    }
}
