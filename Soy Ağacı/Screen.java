import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class Screen extends JFrame {
    private JButton button1;
    private JPanel Panel;
    ArrayList<Kisi> people;
    public Screen(ArrayList<Kisi> peoplelistesi) {
        people=peoplelistesi;
        add(Panel);
        setSize(800,600);
        setTitle("SOY AĞACI");
        button1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                SoyAgaci arayuz2 = new SoyAgaci(people);//yeni arayuz
                arayuz2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                arayuz2.setVisible(true);

            }
   });
}
}