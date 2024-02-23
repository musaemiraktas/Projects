import java.util.*;
public abstract class Nesne {
    private double dayaniklilik,seviyePuani;
    private String isim;

    public Nesne(){


    }

    public double getDayaniklilik() {
        return dayaniklilik;
    }

    public void setDayaniklilik(double dayaniklilik) {
        this.dayaniklilik = dayaniklilik;
    }

    public double getSeviyePuani() {
        return seviyePuani;
    }

    public void setSeviyePuani(double seviyePuani) {
        this.seviyePuani = seviyePuani;
    }

    public String getIsim() {
        return isim;
    }

    public void setIsim(String isim) {
        this.isim = isim;
    }

    public Nesne(double dayaniklilik, double seviyePuani, String isim) {
        this.dayaniklilik=dayaniklilik;
        this.seviyePuani=seviyePuani;
        this.isim = isim;
    }
    public double nesnePuaniGoster() {
        return 0;
    }
    public double  etkiHesapla() {
        return 0;
    }
    public double durumGuncelle() {
        return 0;

    }
}
