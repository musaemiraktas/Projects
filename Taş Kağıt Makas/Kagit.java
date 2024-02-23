public class Kagit extends Nesne {
    double nufuz;

    public Kagit() {
        super();

    }

    public Kagit(double dayaniklilik, double seviyePuani, double nufuz, String isim) {
        super();
        this.nufuz=nufuz;
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

    public double getNufuz() {
        return nufuz;
    }

    public void setNufuz(double nufuz) {
        this.nufuz = nufuz;
    }
}



