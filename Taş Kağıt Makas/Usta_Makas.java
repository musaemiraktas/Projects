public class Usta_Makas extends Makas {
    double direnc;

    public Usta_Makas() {
        super();

    }

    public Usta_Makas(double dayaniklilik, double seviyePuani, double keskinlik, String isim, double direnc) {
        super(dayaniklilik, seviyePuani, keskinlik, isim);
        this.direnc=direnc;
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

    public double getDirenc() {
        return direnc;
    }

    public void setDirenc(double direnc) {
        this.direnc = direnc;
    }
}
