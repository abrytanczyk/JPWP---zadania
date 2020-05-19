import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.InetSocketAddress;
import java.net.Socket;

class DateTime {

    public static void main(String[] args) {

        String address = "time.nist.gov";
        int port = 13;

        /*
        Utwórz gniazdo na porcie przypisanym dla protokołu  DAYTIME, pobierz z niego strumień wejściowy i odczytaj odpowiedź serwera.
        Nie zapomnij o zamknięciu strumienia i gniazda.
        */

        InetSocketAddress socketAddress = new InetSocketAddress(address, port);
        Socket socket = new Socket();
        try {
            socket.connect(socketAddress);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String time = in.readLine();
            socket.shutdownInput();
            socket.shutdownOutput();
            socket.close();
            System.out.println(time);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
