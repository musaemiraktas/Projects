public class Makas extends Nesne {
    double keskinlik;

    public Makas() {
        super();
        // TODO Auto-generated constructor stub
    }

    public Makas(double dayaniklilik, double seviyePuani, double keskinlik, String isim) {
        super(dayaniklilik, seviyePuani, isim);
        this.keskinlik=keskinlik;
    }

    public Makas(double dayaniklilik, double seviyePuani, double keskinlik) {
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


    public double getKeskinlik() {
        return keskinlik;
    }

    public void setKeskinlik(double keskinlik) {
        this.keskinlik = keskinlik;
    }
}

