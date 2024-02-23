public class Oyuncu {

    private int oyuncuID;
    private String oyuncuAdi;
    private double skor;
    public Oyuncu() {
        super();

    }
    public Oyuncu(int oyuncuID, String oyuncuAdi) {
        this.oyuncuID=oyuncuID;
        this.oyuncuAdi=oyuncuAdi;
    }

    public Oyuncu(int oyuncuID, String oyuncuAdi, double skor) {
    }

    public double skorGoster() {
        return 0;
    }
    public String  nesneSec() {// bilgisayar ve kullanıcı icin farklı
        return"e";
    }
}