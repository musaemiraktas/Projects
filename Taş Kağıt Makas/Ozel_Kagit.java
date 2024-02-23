public class Ozel_Kagit extends Kagit {
    double kalinlik;

    public Ozel_Kagit() {
        super();

    }

    public Ozel_Kagit(double dayaniklilik, double seviyePuani, double nufuz, String isim, double kalinlik) {
        super(dayaniklilik, seviyePuani, nufuz, isim);
        this.kalinlik=kalinlik;
    }


    public double nesnePuaniGoster() {

        return super.nesnePuaniGoster();
    }


    public double etkiHesapla() {

        return super.etkiHesapla();
    }

    public double getKalinlik() {
        return kalinlik;
    }

    public void setKalinlik(double kalinlik) {
        this.kalinlik = kalinlik;
    }
}
