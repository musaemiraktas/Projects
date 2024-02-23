import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.Objects;

public class Nesne_Secimi {
    private JButton secim1Button;
    private JButton secim2Button;
    private JButton secim3Button;
    private JButton secim4Button;
    private JButton secim5Button;
    private JButton tasButton;
    private JButton kagitButton;
    private JButton makasButton;
    private JPanel Panel;

    static JFrame f=new JFrame();


    public Nesne_Secimi (){

        ArrayList<String> esyalar = new ArrayList<String>();

        tasButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (Objects.equals(secim1Button.getText(), "Nesne"))
                    secim1Button.setText("Tas");
                else if (Objects.equals(secim2Button.getText(), "Nesne"))
                    secim2Button.setText("Tas");
                else if (Objects.equals(secim3Button.getText(), "Nesne"))
                    secim3Button.setText("Tas");
                else if (Objects.equals(secim4Button.getText(), "Nesne"))
                    secim4Button.setText("Tas");
                else if (Objects.equals(secim5Button.getText(), "Nesne")) {
                    secim5Button.setText("Tas");
                    kagitButton.setText("OYNA!");
                }
            }
        });
        kagitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (Objects.equals(secim1Button.getText(), "Nesne"))
                    secim1Button.setText("Kagit");
                else if (Objects.equals(secim2Button.getText(), "Nesne"))
                    secim2Button.setText("Kagit");
                else if (Objects.equals(secim3Button.getText(), "Nesne"))
                    secim3Button.setText("Kagit");
                else if (Objects.equals(secim4Button.getText(), "Nesne"))
                    secim4Button.setText("Kagit");
                else if (Objects.equals(secim5Button.getText(), "Nesne"))
                    secim5Button.setText("Kagit");


                if (Objects.equals(kagitButton.getText(), "OYNA!")) {
                    esyalar.add(secim1Button.getText());
                    esyalar.add(secim2Button.getText());
                    esyalar.add(secim3Button.getText());
                    esyalar.add(secim4Button.getText());
                    esyalar.add(secim5Button.getText());
                    f.setVisible(false);
                    Bilgisayar_Kullanici bilgisayar_kullanici = new Bilgisayar_Kullanici(esyalar.get(0), esyalar.get(1), esyalar.get(2), esyalar.get(3), esyalar.get(4));
                    bilgisayar_kullanici.bilgisayar_kullanici();
                }

                if (!Objects.equals(secim1Button.getText(), "Nesne") && !Objects.equals(secim2Button.getText(), "Nesne") && !Objects.equals(secim3Button.getText(), "Nesne") && !Objects.equals(secim4Button.getText(), "Nesne") && !Objects.equals(secim5Button.getText(), "Nesne")) {
                    kagitButton.setText("OYNA!");
                }
            }

        });
        makasButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (Objects.equals(secim1Button.getText(), "Nesne"))
                    secim1Button.setText("Makas");
                else if (Objects.equals(secim2Button.getText(), "Nesne"))
                    secim2Button.setText("Makas");
                else if (Objects.equals(secim3Button.getText(), "Nesne"))
                    secim3Button.setText("Makas");
                else if (Objects.equals(secim4Button.getText(), "Nesne"))
                    secim4Button.setText("Makas");
                else if (Objects.equals(secim5Button.getText(), "Nesne"))
                    secim5Button.setText("Makas");
            }
        });

    }

    public static void NesneSecimi() {
        f.setContentPane(new Nesne_Secimi().Panel);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
        f.setSize(1920, 1080);
    }
}