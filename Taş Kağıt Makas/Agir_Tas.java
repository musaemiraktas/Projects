public class Agir_Tas extends Tas {
    double sicaklik;

    public Agir_Tas() {
        super();

    }

    public Agir_Tas(double dayaniklilik, double seviyePuani, double katilik, String isim, double sicaklik) {
        super(dayaniklilik, seviyePuani, katilik, isim);

        this.sicaklik=sicaklik;
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


    public double getSicaklik() {
        return sicaklik;
    }

    public void setSicaklik(double sicaklik) {
        this.sicaklik = sicaklik;
    }
}