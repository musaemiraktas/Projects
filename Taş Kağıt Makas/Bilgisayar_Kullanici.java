import javax.swing.*;
import java.awt.event.ActionListener;
import java.util.Random;
import java.util.ArrayList;
import java.awt.event.ActionEvent;
import java.util.Objects;


public class Bilgisayar_Kullanici {
    private JPanel Panel;
    private JButton button_sec1;
    private JButton button_sec2;
    private JButton button_sec3;
    private JButton button_sec4;
    private JButton button_sec5;
    private JButton nesneButton;
    private JButton nesneButton5;
    private JButton nesneButton3;
    private JButton nesneButton2;
    private JButton nesneButton4;
    private JButton AnaSec1;
    private JButton AnaSec2;
    private JButton onay;

    static JFrame f = new JFrame();
    ArrayList<String> esyalar = new ArrayList<>();
    ArrayList<String> esyalar_2 = new ArrayList<>();
    int sayac = 0;

    public Bilgisayar_Kullanici(String oyuncu1, String oyuncu2, String oyuncu3, String oyuncu4, String oyuncu5) {

        f.setContentPane(Panel);
        Random rnd = new Random();
        ArrayList<String> b = new ArrayList<>();
        ArrayList<String> bil_2 = new ArrayList<>();
        bilgisayar_kullanici();

        esyalar.add(oyuncu1);
        esyalar.add(oyuncu2);
        esyalar.add(oyuncu3);
        esyalar.add(oyuncu4);
        esyalar.add(oyuncu5);

        ArrayList<Agir_Tas> tas_listesi = new ArrayList<Agir_Tas>();
        ArrayList<Ozel_Kagit> kagit_listesi = new ArrayList<Ozel_Kagit>();
        ArrayList<Usta_Makas> makas_listesi = new ArrayList<Usta_Makas>();
        ArrayList<Agir_Tas> bil_tas_listesi = new ArrayList<Agir_Tas>();
        ArrayList<Ozel_Kagit> bil_kagit_listesi = new ArrayList<Ozel_Kagit>();
        ArrayList<Usta_Makas> bil_makas_listesi = new ArrayList<Usta_Makas>();

        for (int i = 0; i < 5; i++) {
            int j = rnd.nextInt(3);
            if (j == 0) {
                b.add("Tas");
            } else if (j == 1) {
                b.add("Kagit");
            } else if (j == 2) {
                b.add("Makas");
            }
        }

        for (int i = 0; i < 5; i++) {
            if (Objects.equals(esyalar.get(i), "Tas")) {
                Agir_Tas tas = new Agir_Tas(20, 0, 2, "Tas", 1);
                tas_listesi.add(tas);
            } else if (Objects.equals(esyalar.get(i), "Makas")) {
                Usta_Makas makas = new Usta_Makas(20, 0, 2, "Makas", 1);
                makas_listesi.add(makas);
            } else if (Objects.equals(esyalar.get(i), "Kagit")) {
                Ozel_Kagit kagit = new Ozel_Kagit(20, 0, 2, "Kagit", 1);
                kagit_listesi.add(kagit);
            }


            if (Objects.equals(b.get(i), "Tas")) {
                Agir_Tas tas = new Agir_Tas(20, 0, 2, "Tas", 1);
                bil_tas_listesi.add(tas);
            }
            if (Objects.equals(b.get(i), "Makas")) {
                Usta_Makas makas = new Usta_Makas(20, 0, 2, "Makas", 1);
                bil_makas_listesi.add(makas);
            }
            if (Objects.equals(b.get(i), "Kagit")) {
                Ozel_Kagit kagit = new Ozel_Kagit(20, 0, 2, "Kagit", 1);
                bil_kagit_listesi.add(kagit);
            }
        }
        int s1 = 1, s2 = 1, s3 = 1;


        for (int i = 0; i < 5; i++) {
            if (Objects.equals(esyalar.get(i), "Tas")) {
                tas_listesi.get(s1 - 1).setIsim("Tas" + s1);
                s1++;
            }
            if (Objects.equals(esyalar.get(i), "Kagit")) {
                kagit_listesi.get(s2 - 1).setIsim("Kagit" + s2);
                s2++;
            }
            if (Objects.equals(esyalar.get(i), "Makas")) {
                makas_listesi.get(s3 - 1).setIsim("Makas" + s3);
                s3++;
            }
        }
        s1= 1;
        s2 = 1;
        s3 = 1;

        for (int i = 0; i < 5; i++) {
            if (Objects.equals(b.get(i), "Tas")) {
                bil_tas_listesi.get(s1- 1).setIsim("Tas" + s1);
                s1++;
            }
            if (Objects.equals(b.get(i), "Kagit")) {
                bil_kagit_listesi.get(s2 - 1).setIsim("Kagit" + s2);
                s2++;
            }
            if (Objects.equals(b.get(i), "Makas")) {
                bil_makas_listesi.get(s3 - 1).setIsim("Makas" + s3);
                s3++;
            }
        }

        s1 = 1;
        s2 = 1;
        s3 = 1;


        for (int i = 0; i < 5; i++) {

            if (Objects.equals(esyalar.get(i), "Tas")) {
                esyalar_2.add("Tas" + s1);
                s1++;
            }
            if (Objects.equals(esyalar.get(i), "Kagit")) {
                esyalar_2.add("Kagit" + s2);
                s2++;
            }
            if (Objects.equals(esyalar.get(i), "Makas")) {
                esyalar_2.add("Makas" + s3);
                s3++;
            }
        }

        s1 = 1;
        s2 = 1;
        s3 = 1;

        for (int i = 0; i < 5; i++) {

            if (Objects.equals(b.get(i), "Tas")) {
                bil_2.add("Tas" + s1);
                s1++;
            }
            if (Objects.equals(b.get(i), "Kagit")) {
                bil_2.add("Kagit" + s2);
                s2++;
            }
            if (Objects.equals(b.get(i), "Makas")) {
                bil_2.add("Makas" + s3);
                s3++;
            }
        }

        button_sec1.setText(esyalar_2.get(0));
        button_sec2.setText(esyalar_2.get(1));
        button_sec3.setText(esyalar_2.get(2));
        button_sec4.setText(esyalar_2.get(3));
        button_sec5.setText(esyalar_2.get(4));


        onay.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Random rnd = new Random();
                int a = rnd.nextInt(4);

                int kazanan = 4;

                AnaSec2.setText(bil_2.get(a));

                String o_click = AnaSec1.getText().substring(0, AnaSec1.getText().length() - 1);

                System.out.println(o_click);

                if ((Objects.equals(o_click, "Tas") && Objects.equals(b.get(a), "Makas")) || (Objects.equals(o_click, "Kagit") && Objects.equals(b.get(a), "Tas")) || (Objects.equals(o_click, "Makas") && Objects.equals(b.get(a), "Kagit"))) {
                    kazanan = 1;
                }
                if ((Objects.equals(o_click, "Tas") && Objects.equals(b.get(a), "Kagit")) || (Objects.equals(o_click, "Kagit") && Objects.equals(b.get(a), "Makas")) || (Objects.equals(o_click, "Makas") && Objects.equals(b.get(a), "Tas"))) {
                    kazanan = 0;
                }
                if ((Objects.equals(o_click, "Tas") && Objects.equals(b.get(a), "Tas")) || (Objects.equals(o_click, "Kagit") && Objects.equals(b.get(a), "Kagit")) || (Objects.equals(o_click, "Makas") && Objects.equals(b.get(a), "Makas"))) {
                    kazanan = 3;
                }

                if(kazanan == 3){
                    if (Objects.equals(o_click, "Tas")){
                        int oyuncu_sira = Integer.parseInt(AnaSec1.getText().substring(AnaSec1.getText().length() - 1)) - 1;
                        int bilgisayar_sira = Integer.parseInt(bil_2.get(a).substring(bil_2.get(a).length() - 1)) - 1;
                        System.out.println(oyuncu_sira);
                        double oyuncu_hasar, bilgisayar_hasar;

                        oyuncu_hasar = (tas_listesi.get(oyuncu_sira).getKatilik() * tas_listesi.get(oyuncu_sira).getSicaklik()) / (bil_tas_listesi.get(bilgisayar_sira).getKatilik() * bil_tas_listesi.get(bilgisayar_sira).getSicaklik() * 0.8);
                        bilgisayar_hasar = (bil_tas_listesi.get(bilgisayar_sira).getKatilik() * bil_tas_listesi.get(bilgisayar_sira).getSicaklik()) / (tas_listesi.get(oyuncu_sira).getKatilik() * tas_listesi.get(oyuncu_sira).getSicaklik() * 0.8);

                        int b = bil_tas_listesi.size();

                        if(sayac < b) {
                            if (tas_listesi.get(oyuncu_sira).getDayaniklilik() == 0) {
                                tas_listesi.get(oyuncu_sira).setDayaniklilik(20);
                            }
                            if (bil_tas_listesi.get(bilgisayar_sira).getDayaniklilik() == 0) {
                                bil_tas_listesi.get(b).setDayaniklilik(20);
                            }
                        }

                        System.out.println(oyuncu_hasar + " " + bilgisayar_hasar);

                        tas_listesi.get(oyuncu_sira).setDayaniklilik(tas_listesi.get(oyuncu_sira).getDayaniklilik() - bilgisayar_hasar);
                        bil_tas_listesi.get(bilgisayar_sira).setDayaniklilik(bil_tas_listesi.get(bilgisayar_sira).getDayaniklilik() - oyuncu_hasar);


                        if (tas_listesi.get(oyuncu_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(tas_listesi.get(oyuncu_sira).getIsim(), esyalar_2.get(i))) {
                                    esyalar.remove(i);
                                    esyalar_2.remove(i);
                                }
                            }
                        }
                        if (bil_tas_listesi.get(bilgisayar_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(bil_tas_listesi.get(bilgisayar_sira).getIsim(), bil_2.get(i))) {

                                    bil_2.remove(i);
                                }
                            }
                        }
                        System.out.println("Rakip :" + bil_tas_listesi.get(bilgisayar_sira).getIsim() + "Dayanıklılık: " + bil_tas_listesi.get(bilgisayar_sira).getDayaniklilik() + " Tecrübe: " + bil_tas_listesi.get(bilgisayar_sira).getSeviyePuani());
                        System.out.println("Kullanici:" + tas_listesi.get(oyuncu_sira).getIsim() + "Dayanıklılık: " + tas_listesi.get(oyuncu_sira).getDayaniklilik() + " Tecrübe: " + tas_listesi.get(oyuncu_sira).getSeviyePuani());

                    }
                    if (Objects.equals(o_click, "Kagit")){

                        int oyuncu_sira = Integer.parseInt(AnaSec1.getText().substring(AnaSec1.getText().length() - 1)) - 1;
                        int bilgisayar_sira = Integer.parseInt(bil_2.get(a).substring(bil_2.get(a).length() - 1)) - 1;
                        double oyuncu_hasar, bilgisayar_hasar;

                        oyuncu_hasar = (kagit_listesi.get(oyuncu_sira).getNufuz() * kagit_listesi.get(oyuncu_sira).getKalinlik()) / (bil_kagit_listesi.get(bilgisayar_sira).getNufuz() * bil_kagit_listesi.get(bilgisayar_sira).getKalinlik() * 0.8);
                        bilgisayar_hasar = (bil_kagit_listesi.get(bilgisayar_sira).getKalinlik() * bil_kagit_listesi.get(bilgisayar_sira).getNufuz()) / (kagit_listesi.get(oyuncu_sira).getNufuz() * kagit_listesi.get(oyuncu_sira).getKalinlik() * 0.8);

                        int b = bil_kagit_listesi.size();

                        if(sayac < b) {
                            if (kagit_listesi.get(oyuncu_sira).getDayaniklilik() == 0) {
                                kagit_listesi.get(oyuncu_sira).setDayaniklilik(20);
                            }
                            if (bil_kagit_listesi.get(bilgisayar_sira).getDayaniklilik() == 0) {
                                bil_kagit_listesi.get(bilgisayar_sira).setDayaniklilik(20);
                            }
                        }

                        System.out.println(oyuncu_sira);
                        System.out.println(bilgisayar_sira);

                        kagit_listesi.get(oyuncu_sira).setDayaniklilik(kagit_listesi.get(oyuncu_sira).getDayaniklilik() - bilgisayar_hasar);
                        bil_kagit_listesi.get(bilgisayar_sira).setDayaniklilik(bil_kagit_listesi.get(bilgisayar_sira).getDayaniklilik() - oyuncu_hasar);

                        System.out.println(oyuncu_sira);
                        if (kagit_listesi.get(oyuncu_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(kagit_listesi.get(oyuncu_sira).getIsim(), esyalar_2.get(i))) {
                                    esyalar.remove(i);
                                    esyalar_2.remove(i);
                                }
                            }
                        }
                        if (bil_kagit_listesi.get(bilgisayar_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(bil_kagit_listesi.get(bilgisayar_sira).getIsim(), bil_2.get(i))) {

                                    bil_2.remove(i);
                                }
                            }
                        }
                        System.out.println("Rakip :" + bil_kagit_listesi.get(bilgisayar_sira).getIsim() + "Dayanıklılık: " + bil_kagit_listesi.get(bilgisayar_sira).getDayaniklilik() + " Tecrübe: " + bil_kagit_listesi.get(bilgisayar_sira).getSeviyePuani());
                        System.out.println("Kullanici:" + kagit_listesi.get(oyuncu_sira).getIsim() + "Dayanıklılık: " + kagit_listesi.get(oyuncu_sira).getDayaniklilik() + " Tecrübe: " + kagit_listesi.get(oyuncu_sira).getSeviyePuani());

                    }
                    if (Objects.equals(o_click, "Makas")){

                        {

                            int oyuncu_sira = Integer.parseInt(AnaSec1.getText().substring(AnaSec1.getText().length() - 1)) - 1;
                            int bilgisayar_sira = Integer.parseInt(bil_2.get(a).substring(bil_2.get(a).length() - 1)) - 1;
                            double oyuncu_hasar, bilgisayar_hasar;

                            oyuncu_hasar =( makas_listesi.get(oyuncu_sira).getKeskinlik() * makas_listesi.get(oyuncu_sira).getSeviyePuani()) / (bil_makas_listesi.get(bilgisayar_sira).getKeskinlik() * bil_makas_listesi.get(bilgisayar_sira).getDirenc()) * 0.8;
                            bilgisayar_hasar = (bil_makas_listesi.get(bilgisayar_sira).getDirenc() * bil_makas_listesi.get(bilgisayar_sira).getKeskinlik()) / (makas_listesi.get(oyuncu_sira).getDirenc() * makas_listesi.get(oyuncu_sira).getKeskinlik() * 0.8);

                            int b = bil_kagit_listesi.size();

                            if(sayac < b) {
                                if (makas_listesi.get(oyuncu_sira).getDayaniklilik() == 0) {
                                    makas_listesi.get(oyuncu_sira).setDayaniklilik(20);
                                }
                                if (bil_makas_listesi.get(bilgisayar_sira).getDayaniklilik() == 0) {
                                    bil_makas_listesi.get(b).setDayaniklilik(20);
                                }
                            }

                            makas_listesi.get(oyuncu_sira).setDayaniklilik(makas_listesi.get(oyuncu_sira).getDayaniklilik() - bilgisayar_hasar);
                            bil_makas_listesi.get(bilgisayar_sira).setDayaniklilik(bil_makas_listesi.get(bilgisayar_sira).getDayaniklilik() - oyuncu_hasar);

                            if (makas_listesi.get(oyuncu_sira).getDayaniklilik() <= 0 && sayac > 10) {
                                for (int i = 0; i < 5; i++) {
                                    if (Objects.equals(makas_listesi.get(oyuncu_sira).getIsim(), esyalar_2.get(i))) {
                                        esyalar.remove(i);
                                        esyalar_2.remove(i);
                                    }
                                }
                            }
                            if (bil_makas_listesi.get(bilgisayar_sira).getDayaniklilik() <= 0 && sayac > 10) {
                                for (int i = 0; i < 5; i++) {
                                    if (Objects.equals(bil_makas_listesi.get(bilgisayar_sira).getIsim(), bil_2.get(i))) {

                                        bil_2.remove(i);
                                    }
                                }
                            }
                            System.out.println("Rakip :" + bil_makas_listesi.get(bilgisayar_sira).getIsim() + "Dayanıklılık: " + bil_makas_listesi.get(bilgisayar_sira).getDayaniklilik() + " Tecrübe: " + bil_makas_listesi.get(bilgisayar_sira).getSeviyePuani());
                            System.out.println("Kullanici:" + makas_listesi.get(oyuncu_sira).getIsim() + "Dayanıklılık: " + makas_listesi.get(oyuncu_sira).getDayaniklilik() + " Tecrübe: " + makas_listesi.get(oyuncu_sira).getSeviyePuani());

                        }
                    }
                }


                if (kazanan == 1) {
                    int oyuncu_sira = Integer.parseInt(AnaSec1.getText().substring(AnaSec1.getText().length() - 1)) - 1;
                    int bilgisayar_sira = Integer.parseInt(bil_2.get(a).substring(bil_2.get(a).length() - 1))-1;
                    if (Objects.equals(o_click, "Tas")) {
                        tas_listesi.get(oyuncu_sira).setSeviyePuani(tas_listesi.get(oyuncu_sira).getSeviyePuani() + 20);
                        double oyuncu_hasar, bilgisayar_hasar;

                        oyuncu_hasar = (tas_listesi.get(oyuncu_sira).getKatilik() * tas_listesi.get(oyuncu_sira).getSicaklik()) / (bil_makas_listesi.get(bilgisayar_sira).getKeskinlik() * bil_makas_listesi.get(bilgisayar_sira).getDirenc() * 0.2);
                        bilgisayar_hasar = (bil_makas_listesi.get(bilgisayar_sira).getDirenc() * bil_makas_listesi.get(bilgisayar_sira).getKeskinlik()) / (tas_listesi.get(oyuncu_sira).getKatilik() * tas_listesi.get(oyuncu_sira).getSicaklik() * 0.8);

                        int b = bil_makas_listesi.size();

                        if(sayac < b) {
                            if (tas_listesi.get(oyuncu_sira).getDayaniklilik() == 0) {
                                tas_listesi.get(oyuncu_sira).setDayaniklilik(20);
                            }
                            if (bil_makas_listesi.get(bilgisayar_sira).getDayaniklilik() == 0) {
                                bil_makas_listesi.get(b).setDayaniklilik(20);
                            }
                        }

                        tas_listesi.get(oyuncu_sira).setDayaniklilik(tas_listesi.get(oyuncu_sira).getDayaniklilik() - bilgisayar_hasar);
                        bil_makas_listesi.get(bilgisayar_sira).setDayaniklilik(bil_makas_listesi.get(bilgisayar_sira).getDayaniklilik() - oyuncu_hasar);

                        if (tas_listesi.get(oyuncu_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(tas_listesi.get(oyuncu_sira).getIsim(), esyalar_2.get(i))) {
                                    esyalar.remove(i);
                                    esyalar_2.remove(i);
                                }
                            }
                        }
                        if (bil_makas_listesi.get(bilgisayar_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(bil_makas_listesi.get(bilgisayar_sira).getIsim(), bil_2.get(i))) {

                                    bil_2.remove(i);
                                }
                            }
                        }
                        if (tas_listesi.get(oyuncu_sira).getSeviyePuani() >= 30) {
                            for (int i = 0; i < 5; i++) {
                                Agir_Tas tas = new Agir_Tas(tas_listesi.get(oyuncu_sira).getDayaniklilik(), 40, 2, tas_listesi.get(oyuncu_sira).getIsim(), 2);
                                tas_listesi.remove(oyuncu_sira);
                                tas_listesi.add(oyuncu_sira, tas);
                            }
                        }
                        System.out.println("Rakip :" + bil_makas_listesi.get(bilgisayar_sira).getIsim() + "Dayanıklılık: " + bil_makas_listesi.get(bilgisayar_sira).getDayaniklilik() + " Tecrübe: " + bil_makas_listesi.get(bilgisayar_sira).getSeviyePuani());
                        System.out.println("Kullanici:" + tas_listesi.get(oyuncu_sira).getIsim() + "Dayanıklılık: " + tas_listesi.get(oyuncu_sira).getDayaniklilik() + " Tecrübe: " + tas_listesi.get(oyuncu_sira).getSeviyePuani());
                    }
                }
                if (kazanan == 0) {
                    int oyuncu_sira = Integer.parseInt(AnaSec1.getText().substring(AnaSec1.getText().length() - 1))-1;
                    int bilgisayar_sira = Integer.parseInt(bil_2.get(a).substring(bil_2.get(a).length() - 1))-1;
                    if (Objects.equals(o_click, "Tas")) {
                        bil_kagit_listesi.get(bilgisayar_sira).setSeviyePuani(bil_kagit_listesi.get(bilgisayar_sira).getSeviyePuani() + 20);

                        System.out.println(oyuncu_sira);

                        double oyuncu_hasar, bilgisayar_hasar;

                        oyuncu_hasar = (tas_listesi.get(oyuncu_sira).getKatilik() * tas_listesi.get(oyuncu_sira).getSicaklik()) / (bil_kagit_listesi.get(bilgisayar_sira).getNufuz() * bil_kagit_listesi.get(bilgisayar_sira).getKalinlik() * 0.8);
                        bilgisayar_hasar = (bil_kagit_listesi.get(bilgisayar_sira).getKalinlik() * bil_kagit_listesi.get(bilgisayar_sira).getKalinlik()) / (tas_listesi.get(oyuncu_sira).getKatilik() * tas_listesi.get(oyuncu_sira).getSicaklik() * 0.2);


                        int b = bil_kagit_listesi.size();

                        if(sayac < b) {
                            if (tas_listesi.get(oyuncu_sira).getDayaniklilik() == 0) {
                                tas_listesi.get(oyuncu_sira).setDayaniklilik(20);
                            }
                            if (bil_kagit_listesi.get(bilgisayar_sira).getDayaniklilik() == 0) {
                                bil_kagit_listesi.get(bilgisayar_sira).setDayaniklilik(20);
                            }
                        }

                        tas_listesi.get(oyuncu_sira).setDayaniklilik(tas_listesi.get(oyuncu_sira).getDayaniklilik() - bilgisayar_hasar);
                        bil_kagit_listesi.get(bilgisayar_sira).setDayaniklilik(bil_kagit_listesi.get(bilgisayar_sira).getDayaniklilik() - oyuncu_hasar);

                        if (tas_listesi.get(oyuncu_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(tas_listesi.get(oyuncu_sira).getIsim(), esyalar_2.get(i))) {
                                    esyalar.remove(i);
                                    esyalar_2.remove(i);
                                }
                            }
                        }
                        if (bil_kagit_listesi.get(bilgisayar_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(bil_kagit_listesi.get(bilgisayar_sira).getIsim(), bil_2.get(i))) {
                                    bil_2.remove(i);
                                }
                            }
                        }
                        if (bil_kagit_listesi.get(bilgisayar_sira).getSeviyePuani() >= 30) {
                            for (int i = 0; i < 5; i++) {
                                Ozel_Kagit kagit = new Ozel_Kagit(bil_kagit_listesi.get(oyuncu_sira).getDayaniklilik(), 40, 2, bil_kagit_listesi.get(oyuncu_sira).getIsim(), 2);
                                bil_kagit_listesi.remove(a);
                                bil_kagit_listesi.add(a, kagit);
                            }
                        }
                        System.out.println("Rakip :" + bil_kagit_listesi.get(bilgisayar_sira).getIsim() + "Dayanıklılık: " + bil_kagit_listesi.get(bilgisayar_sira).getDayaniklilik() + " Tecrübe: " + bil_kagit_listesi.get(bilgisayar_sira).getSeviyePuani());
                        System.out.println("Kullanici:" + tas_listesi.get(oyuncu_sira).getIsim() + "Dayanıklılık: " + tas_listesi.get(oyuncu_sira).getDayaniklilik() + " Tecrübe: " + tas_listesi.get(oyuncu_sira).getSeviyePuani());
                    }
                }

                if (kazanan == 1) {
                    int oyuncu_sira = Integer.parseInt(AnaSec1.getText().substring(AnaSec1.getText().length() - 1)) - 1;
                    int bilgisayar_sira = Integer.parseInt(bil_2.get(a).substring(bil_2.get(a).length() - 1)) - 1;
                    if (Objects.equals(o_click, "Kagit")) {
                        kagit_listesi.get(oyuncu_sira).setSeviyePuani(kagit_listesi.get(oyuncu_sira).getSeviyePuani() + 20);
                        double oyuncu_hasar, bilgisayar_hasar;

                        oyuncu_hasar = (kagit_listesi.get(oyuncu_sira).getKalinlik() * kagit_listesi.get(oyuncu_sira).getNufuz()) / (bil_tas_listesi.get(bilgisayar_sira).getSicaklik() * bil_tas_listesi.get(bilgisayar_sira).getKatilik() * 0.2);
                        bilgisayar_hasar = (bil_tas_listesi.get(bilgisayar_sira).getKatilik() * bil_tas_listesi.get(bilgisayar_sira).getSicaklik()) / (kagit_listesi.get(oyuncu_sira).getKalinlik() * kagit_listesi.get(oyuncu_sira).getNufuz() * 0.8);

                        int b = bil_kagit_listesi.size();

                        if(sayac < b) {
                            if (kagit_listesi.get(oyuncu_sira).getDayaniklilik() == 0) {
                                kagit_listesi.get(oyuncu_sira).setDayaniklilik(20);
                            }
                            if (bil_tas_listesi.get(bilgisayar_sira).getDayaniklilik() == 0) {
                                bil_tas_listesi.get(b).setDayaniklilik(20);
                            }
                        }

                        kagit_listesi.get(oyuncu_sira).setDayaniklilik(kagit_listesi.get(oyuncu_sira).getDayaniklilik() - bilgisayar_hasar);
                        bil_tas_listesi.get(bilgisayar_sira).setDayaniklilik(bil_tas_listesi.get(bilgisayar_sira).getDayaniklilik() - oyuncu_hasar);

                        if (kagit_listesi.get(oyuncu_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(kagit_listesi.get(oyuncu_sira).getIsim(), esyalar_2.get(i))) {
                                    esyalar_2.remove(i);
                                }
                            }
                        }
                        if (bil_tas_listesi.get(bilgisayar_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(bil_tas_listesi.get(bilgisayar_sira).getIsim(), bil_2.get(i))) {

                                    bil_2.remove(i);
                                }
                            }
                        }
                        if (kagit_listesi.get(oyuncu_sira).getSeviyePuani() >= 30) {
                            for (int i = 0; i < 5; i++) {
                                Ozel_Kagit tas = new Ozel_Kagit(kagit_listesi.get(oyuncu_sira).getDayaniklilik(), 40, 2, kagit_listesi.get(oyuncu_sira).getIsim(), 2);
                                kagit_listesi.remove(oyuncu_sira);
                                kagit_listesi.add(oyuncu_sira, tas);
                            }
                        }
                        System.out.println("Rakip :" + bil_tas_listesi.get(bilgisayar_sira).getIsim() + "Dayanıklılık: " + bil_tas_listesi.get(bilgisayar_sira).getDayaniklilik() + " Tecrübe: " + bil_tas_listesi.get(bilgisayar_sira).getSeviyePuani());
                        System.out.println("Kullanici:" + kagit_listesi.get(oyuncu_sira).getIsim() + "Dayanıklılık: " + kagit_listesi.get(oyuncu_sira).getDayaniklilik() + " Tecrübe: " + kagit_listesi.get(oyuncu_sira).getSeviyePuani());
                    }
                }

                if (kazanan == 0) {
                    int oyuncu_sira = Integer.parseInt(AnaSec1.getText().substring(AnaSec1.getText().length() - 1))-1;
                    int bilgisayar_sira = Integer.parseInt(bil_2.get(a).substring(bil_2.get(a).length() - 1))-1;
                    if (Objects.equals(o_click, "Kagit")) {
                        bil_makas_listesi.get(bilgisayar_sira).setSeviyePuani(bil_makas_listesi.get(bilgisayar_sira).getSeviyePuani() + 20);

                        double oyuncu_hasar, bilgisayar_hasar;

                        oyuncu_hasar =(kagit_listesi.get(oyuncu_sira).getKalinlik() * kagit_listesi.get(oyuncu_sira).getNufuz()) / (bil_makas_listesi.get(bilgisayar_sira).getDirenc() * bil_makas_listesi.get(bilgisayar_sira).getKeskinlik() * 0.8);
                        bilgisayar_hasar = (bil_makas_listesi.get(bilgisayar_sira).getDirenc() * bil_makas_listesi.get(bilgisayar_sira).getKeskinlik()) / (kagit_listesi.get(oyuncu_sira).getNufuz() * kagit_listesi.get(oyuncu_sira).getKalinlik() * 0.2);

                        int b = bil_makas_listesi.size();

                        if(sayac < b) {
                            if (kagit_listesi.get(oyuncu_sira).getDayaniklilik() == 0) {
                                kagit_listesi.get(oyuncu_sira).setDayaniklilik(20);
                            }
                            if (bil_makas_listesi.get(bilgisayar_sira).getDayaniklilik() == 0) {
                                bil_makas_listesi.get(bilgisayar_sira).setDayaniklilik(20);
                            }
                        }

                        kagit_listesi.get(oyuncu_sira).setDayaniklilik(kagit_listesi.get(oyuncu_sira).getDayaniklilik() - bilgisayar_hasar);
                        bil_makas_listesi.get(bilgisayar_sira).setDayaniklilik(bil_makas_listesi.get(bilgisayar_sira).getDayaniklilik() - oyuncu_hasar);

                        if (kagit_listesi.get(oyuncu_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                System.out.println(kagit_listesi.get(oyuncu_sira).getIsim());
                                if (Objects.equals(kagit_listesi.get(oyuncu_sira).getIsim(), esyalar_2.get(i))) {
                                    esyalar.remove(i);
                                    esyalar_2.remove(i);
                                }
                            }
                        }
                        if (bil_makas_listesi.get(bilgisayar_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(bil_makas_listesi.get(bilgisayar_sira).getIsim(), bil_2.get(i))) {
                                    bil_2.remove(i);
                                }
                            }
                        }
                        if (bil_makas_listesi.get(bilgisayar_sira).getSeviyePuani() >= 30) {
                            for (int i = 0; i < 5; i++) {
                                Usta_Makas makas = new Usta_Makas(bil_makas_listesi.get(oyuncu_sira).getDayaniklilik(), 40, 2, bil_makas_listesi.get(oyuncu_sira).getIsim(), 2);
                                bil_makas_listesi.remove(a);
                                bil_makas_listesi.add(a, makas);
                            }
                        }
                        System.out.println("Rakip :" + bil_makas_listesi.get(bilgisayar_sira).getIsim() + "Dayanıklılık: " + bil_makas_listesi.get(bilgisayar_sira).getDayaniklilik() + " Tecrübe: " + bil_makas_listesi.get(bilgisayar_sira).getSeviyePuani());
                        System.out.println("Kullanici:" + kagit_listesi.get(oyuncu_sira).getIsim() + "Dayanıklılık: " + kagit_listesi.get(oyuncu_sira).getDayaniklilik() + " Tecrübe: " + kagit_listesi.get(oyuncu_sira).getSeviyePuani());
                    }
                }

                if (kazanan == 1) {
                    int oyuncu_sira = Integer.parseInt(AnaSec1.getText().substring(AnaSec1.getText().length() - 1))-1;
                    int bilgisayar_sira = Integer.parseInt(bil_2.get(a).substring(bil_2.get(a).length() - 1))-1;
                    if (Objects.equals(o_click, "Makas")) {
                        makas_listesi.get(oyuncu_sira).setSeviyePuani(makas_listesi.get(oyuncu_sira).getSeviyePuani() + 20);

                        double oyuncu_hasar, bilgisayar_hasar;

                        oyuncu_hasar =( makas_listesi.get(oyuncu_sira).getDirenc() * makas_listesi.get(oyuncu_sira).getKeskinlik()) / (bil_kagit_listesi.get(bilgisayar_sira).getNufuz() * bil_kagit_listesi.get(bilgisayar_sira).getKalinlik() * 0.2);
                        bilgisayar_hasar = (bil_kagit_listesi.get(bilgisayar_sira).getKalinlik() * bil_kagit_listesi.get(bilgisayar_sira).getNufuz()) / (makas_listesi.get(oyuncu_sira).getKeskinlik() * makas_listesi.get(oyuncu_sira).getDirenc() * 0.8);

                        int b = bil_kagit_listesi.size();

                        if(sayac < b) {
                            if (makas_listesi.get(oyuncu_sira).getDayaniklilik() == 0) {
                                makas_listesi.get(oyuncu_sira).setDayaniklilik(20);
                            }
                            if (bil_kagit_listesi.get(bilgisayar_sira).getDayaniklilik() == 0) {
                                bil_kagit_listesi.get(b).setDayaniklilik(20);
                            }
                        }

                        makas_listesi.get(oyuncu_sira).setDayaniklilik(makas_listesi.get(oyuncu_sira).getDayaniklilik() - bilgisayar_hasar);
                        bil_kagit_listesi.get(bilgisayar_sira).setDayaniklilik(bil_kagit_listesi.get(bilgisayar_sira).getDayaniklilik() - oyuncu_hasar);

                        if (makas_listesi.get(oyuncu_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(makas_listesi.get(oyuncu_sira).getIsim(), esyalar_2.get(i))) {
                                    esyalar.remove(i);
                                    esyalar_2.remove(i);
                                }
                            }
                        }
                        if (bil_kagit_listesi.get(bilgisayar_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(bil_kagit_listesi.get(bilgisayar_sira).getIsim(), bil_2.get(i))) {

                                    bil_2.remove(i);
                                }
                            }
                        }
                        if (makas_listesi.get(oyuncu_sira).getSeviyePuani() >= 30) {
                            for (int i = 0; i < 5; i++) {
                                Usta_Makas tas = new Usta_Makas(makas_listesi.get(oyuncu_sira).getDayaniklilik(), 40, 2, makas_listesi.get(oyuncu_sira).getIsim(), 2);
                                makas_listesi.remove(oyuncu_sira);
                                makas_listesi.add(oyuncu_sira, tas);
                            }
                        }
                        System.out.println("Rakip :" + bil_kagit_listesi.get(bilgisayar_sira).getIsim() + "Dayanıklılık: " + bil_kagit_listesi.get(bilgisayar_sira).getDayaniklilik() + " Tecrübe: " + bil_kagit_listesi.get(bilgisayar_sira).getSeviyePuani());
                        System.out.println("Kullanici:" + makas_listesi.get(oyuncu_sira).getIsim() + "Dayanıklılık: " + makas_listesi.get(oyuncu_sira).getDayaniklilik() + " Tecrübe: " + makas_listesi.get(oyuncu_sira).getSeviyePuani());
                    }
                }
                if (kazanan == 0) {
                    int oyuncu_sira = Integer.parseInt(AnaSec1.getText().substring(AnaSec1.getText().length() - 1)) -1;
                    int bilgisayar_sira = Integer.parseInt(bil_2.get(a).substring(bil_2.get(a).length() - 1))-1;
                    if (Objects.equals(o_click, "Makas")) {
                        bil_tas_listesi.get(bilgisayar_sira).setSeviyePuani(bil_tas_listesi.get(bilgisayar_sira).getSeviyePuani() + 20);

                        double oyuncu_hasar, bilgisayar_hasar;

                        oyuncu_hasar = (makas_listesi.get(oyuncu_sira).getDirenc() * makas_listesi.get(oyuncu_sira).getKeskinlik()) / (bil_tas_listesi.get(bilgisayar_sira).getKatilik() * bil_tas_listesi.get(bilgisayar_sira).getSicaklik() * 0.8);
                        bilgisayar_hasar = (bil_tas_listesi.get(bilgisayar_sira).getKatilik() * bil_tas_listesi.get(bilgisayar_sira).getSicaklik()) / (makas_listesi.get(oyuncu_sira).getDirenc() * makas_listesi.get(oyuncu_sira).getKeskinlik() * 0.2);

                        int b = bil_kagit_listesi.size();

                        if(sayac < b) {
                            if (makas_listesi.get(oyuncu_sira).getDayaniklilik() == 0) {
                                makas_listesi.get(oyuncu_sira).setDayaniklilik(20);
                            }
                            if (bil_tas_listesi.get(bilgisayar_sira).getDayaniklilik() == 0) {
                                bil_tas_listesi.get(b).setDayaniklilik(20);
                            }
                        }

                        makas_listesi.get(oyuncu_sira).setDayaniklilik(makas_listesi.get(oyuncu_sira).getDayaniklilik() - bilgisayar_hasar);
                        bil_tas_listesi.get(bilgisayar_sira).setDayaniklilik(bil_tas_listesi.get(bilgisayar_sira).getDayaniklilik() - oyuncu_hasar);

                        if (makas_listesi.get(oyuncu_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(makas_listesi.get(oyuncu_sira).getIsim(), esyalar_2.get(i))) {
                                    esyalar.remove(i);
                                    esyalar_2.remove(i);
                                }
                            }
                        }
                        if (bil_tas_listesi.get(bilgisayar_sira).getDayaniklilik() <= 0 && sayac > 10) {
                            for (int i = 0; i < 5; i++) {
                                if (Objects.equals(bil_tas_listesi.get(bilgisayar_sira).getIsim(), bil_2.get(i))) {

                                    bil_2.remove(i);
                                }
                            }
                        }
                        if (bil_tas_listesi.get(bilgisayar_sira).getSeviyePuani() >= 30) {
                            for (int i = 0; i < 5; i++) {
                                Agir_Tas tas = new Agir_Tas(bil_tas_listesi.get(oyuncu_sira).getDayaniklilik(), 40, 2, bil_tas_listesi.get(oyuncu_sira).getIsim(), 2);
                                bil_tas_listesi.remove(a);
                                bil_tas_listesi.add(a, tas);
                            }
                        }
                        System.out.println("Rakip :" + bil_tas_listesi.get(bilgisayar_sira).getIsim() + "Dayanıklılık: " + bil_tas_listesi.get(bilgisayar_sira).getDayaniklilik() + " Tecrübe: " + bil_tas_listesi.get(bilgisayar_sira).getSeviyePuani());
                        System.out.println("Kullanici:" + makas_listesi.get(oyuncu_sira).getIsim() + "Dayanıklılık: " + makas_listesi.get(oyuncu_sira).getDayaniklilik() + " Tecrübe: " + makas_listesi.get(oyuncu_sira).getSeviyePuani());
                    }
                }
                sayac++;
            }


        });
            button_sec1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                AnaSec1.setText(button_sec1.getText());
            }
        });
        button_sec2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                AnaSec1.setText(button_sec2.getText());
            }
        });
        button_sec3.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                AnaSec1.setText(button_sec3.getText());
            }
        });
        button_sec4.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                AnaSec1.setText(button_sec4.getText());
            }
        });
        button_sec5.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                AnaSec1.setText(button_sec5.getText());
            }
        });
    }

    public static void bilgisayar_kullanici () {
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
        f.setSize(1920, 1080);
    }

}

