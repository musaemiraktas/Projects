import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.Objects;

public class SoyAgaci extends JFrame {
    private JPanel panel;
    static JLabel[] label;
    ArrayList<Kisi> people;
    public SoyAgaci(ArrayList<Kisi> people1){
        people=people1;
        label = new JLabel[500];
        add(panel);
        setSize(1400,700);
        setTitle("AGAC");
        int a=0,j=0;
        for (int i = 0; i <people.size() ; i++) {

            if (people.get(i) != null) {
                label[a] = new JLabel(people.get(i).getAd()+" "+people.get(i).getSoyad());


                label[a].setFont(new Font("Fira Code", Font.PLAIN, 11));

                label[a].setBounds(525, 5 + (j * 25), 200, 50);
                label[a].setBackground(Color.PINK);

                getContentPane().add(label[a]);
                getContentPane().repaint();
                a++;
            }
            j++;
        }
    }
}