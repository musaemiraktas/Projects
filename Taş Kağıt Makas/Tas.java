
public class Tas extends Nesne {
    double katilik;
    public Tas() {
        super();
    }
    public Tas(double dayaniklilik, double seviyePuani, double katilik, String isim) {
        super(dayaniklilik, seviyePuani, isim);
        this.katilik = katilik;

    }

    public Tas(double dayaniklilik, double seviyePuani, double katilik) {
    }


    public double nesnePuaniGoster() {

        return super.nesnePuaniGoster();
    }

    public double etkiHesapla() {

        return super.etkiHesapla();
    }

    public double durumGuncelle() {

        return super.durumGuncelle();
    }


    public double getKatilik() {
        return katilik;
    }

    public void setKatilik(double katilik) {
        this.katilik = katilik;
    }
}
