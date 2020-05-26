import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ClientGUI {
    private JPanel panel;
    private JTextField infoTxt;
    private JTextField memesTxT;
    private JTextField newsletterTxt;
    private JButton infoButton;
    private JButton memesButton;
    private JButton newsletterButton;
    Client client = new Client();

    public ClientGUI() {
        infoButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (!infoTxt.getText().isEmpty()){
                    client.connection("infos", "Wiadomości", infoTxt.getText());
                } else {
                    JOptionPane.showMessageDialog(null, "Nie podano żądanej frazy!");
                }
                //Clear TextField
                infoTxt.setText("");
            }
        });
        memesButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (!memesTxT.getText().isEmpty()){
                    //Check if given value is an integer
                    try{
                        int amount = Integer.parseInt(memesTxT.getText());
                        client.connection("memes", "Memy", memesTxT.getText());
                    } catch (Exception ex){
                        JOptionPane.showMessageDialog(null, "Błąd! Podaj liczbę!");
                    }
                } else {
                    JOptionPane.showMessageDialog(null, "Nie podano zadanej ilości!");
                }
                //Clear TextField
                memesTxT.setText("");
            }
        });
        newsletterButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (!newsletterTxt.getText().isEmpty()){
                    //Check if given value is a correct e-mail address
                    if (newsletterTxt.getText().matches("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:" +
                            "[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")){
                        client.connection("subscription", "Null", newsletterTxt.getText());
                        JOptionPane.showMessageDialog(null, "Adres: " + newsletterTxt.getText()
                            + " został pomyślnie dopisany do newslettera");
                    } else {
                        JOptionPane.showMessageDialog(null, "Błąd! Podano błędny adres email!");
                    }
                } else {
                    JOptionPane.showMessageDialog(null, "Nie podano adresu email!");
                }
                //Clear TextField
                newsletterTxt.setText("");
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("ClientGUI");
        frame.setContentPane(new ClientGUI().panel);
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
        ClientGUI gui = new ClientGUI();
        frame.setLocationRelativeTo(null);
    }
}
