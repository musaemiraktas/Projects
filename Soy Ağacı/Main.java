import org.apache.poi.ss.usermodel.CellType;
import org.apache.poi.xssf.usermodel.*;

import javax.swing.*;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.Scanner;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        FileInputStream file = new FileInputStream("C:\\Users\\Emir\\Desktop\\Prolab 3 (1).xlsx");

        XSSFWorkbook workbook = new XSSFWorkbook(file);





        ArrayList<Kisi> kisilistesi = new ArrayList<>();
        ArrayList people = new ArrayList();
        Kisi kisi[]= new Kisi[100];
        int personList=0;

        for (int t = 0; t < workbook.getNumberOfSheets(); t++) {
            XSSFSheet sheet = workbook.getSheetAt(t);
            int rowCount = sheet.getLastRowNum();
            int colCount = sheet.getRow(t).getLastCellNum();
            for (int i = 1; i <= rowCount; i++) {
                kisi[personList] = new Kisi();
                XSSFRow currentRow = sheet.getRow(i);

                for (int j = 0; j < colCount; j++) {
                    XSSFCell currentCell = currentRow.getCell(j);

                    if (currentCell.getCellType() == CellType.STRING) {
                        people.add(currentCell.getStringCellValue());
                    } else if (currentCell.getCellType() == CellType.NUMERIC) {
                        if (currentCell.getNumericCellValue() > 1000) {
                            people.add(currentCell.getLocalDateTimeCellValue());
                        } else {
                            people.add(currentCell.getNumericCellValue());

                        }
                    }
                }
                System.out.println();

                if(people.size()==12 && people.get(people.size()-1).equals("Erkek")){

                    kisi[personList].setTcno((Double) people.get(0));
                    kisi[personList].setAd((String) people.get(1));
                    kisi[personList].setSoyad((String) people.get(2));
                    kisi[personList].setDogumTarihi(people.get(3).toString());
                    kisi[personList].setEsi((String) people.get(4));
                    kisi[personList].setEsid((Double) people.get(5));
                    kisi[personList].setAnneAdi((String) people.get(6));
                    kisi[personList].setBabaAdi((String) people.get(7));
                    kisi[personList].setKanGrubu((String) people.get(8));
                    kisi[personList].setMeslek((String) people.get(9));
                    kisi[personList].setCinsiyet((String) people.get(11));
                }
                else if(people.size()==10 && people.get(people.size()-1).equals("Erkek")){

                    kisi[personList].setTcno((Double) people.get(0));
                    kisi[personList].setAd((String) people.get(1));
                    kisi[personList].setSoyad((String) people.get(2));
                    kisi[personList].setDogumTarihi(people.get(3).toString());
                    kisi[personList].setAnneAdi((String) people.get(4));
                    kisi[personList].setBabaAdi((String) people.get(5));
                    kisi[personList].setKanGrubu((String) people.get(6));
                    kisi[personList].setMeslek((String) people.get(7));
                    kisi[personList].setCinsiyet((String) people.get(9));
                }
                else if(people.size()==9){

                    kisi[personList].setTcno((Double) people.get(0));
                    kisi[personList].setAd((String) people.get(1));
                    kisi[personList].setSoyad((String) people.get(2));
                    kisi[personList].setDogumTarihi(people.get(3).toString());
                    kisi[personList].setAnneAdi((String) people.get(4));
                    kisi[personList].setBabaAdi((String) people.get(5));
                    kisi[personList].setKanGrubu((String) people.get(6));
                    kisi[personList].setCinsiyet((String) people.get(8));
                }
                else if(people.size()==13 && people.get(people.size()-1).equals("Kadın")){

                    kisi[personList].setTcno((Double) people.get(0));
                    kisi[personList].setAd((String) people.get(1));
                    kisi[personList].setSoyad((String) people.get(2));
                    kisi[personList].setDogumTarihi(people.get(3).toString());
                    kisi[personList].setEsi((String) people.get(4));
                    kisi[personList].setEsid((Double) people.get(5));
                    kisi[personList].setAnneAdi((String) people.get(6));
                    kisi[personList].setBabaAdi((String) people.get(7));
                    kisi[personList].setKanGrubu((String) people.get(8));
                    kisi[personList].setMeslek((String) people.get(9));
                    kisi[personList].setKizlikSoyadi((String) people.get(11));
                    kisi[personList].setCinsiyet((String) people.get(12));
                }
                else if(people.size()==10 && people.get(people.size()-1).equals("Kadın")){

                    kisi[personList].setTcno((Double) people.get(0));
                    kisi[personList].setAd((String) people.get(1));
                    kisi[personList].setSoyad((String) people.get(2));
                    kisi[personList].setDogumTarihi(people.get(3).toString());
                    kisi[personList].setAnneAdi((String) people.get(4));
                    kisi[personList].setBabaAdi((String) people.get(5));
                    kisi[personList].setKanGrubu((String) people.get(6));
                    kisi[personList].setMeslek((String) people.get(7));
                    kisi[personList].setCinsiyet((String) people.get(9));
                }
                people.clear();
                kisilistesi.add(kisi[personList]);
                personList++;



            }

            System.out.println();

            }

            System.out.println(kisilistesi.size());
            for (int i = 0; i < kisilistesi.size(); i++) {
                for (int j = i + 1; j < kisilistesi.size(); j++) {
                    if (kisilistesi.get(i).getTcno() == kisilistesi.get(j).getTcno()) {
                        kisilistesi.remove(j);
                    }
                }
                if (kisilistesi.get(i).getTcno() == 0.0) {
                    kisilistesi.remove(i);
                }
            }
            Screen arayuz1 = new Screen(kisilistesi);
            arayuz1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            arayuz1.setVisible(true);





        for(int v=0; v<workbook.getNumberOfSheets(); v++) {
            XSSFSheet sheet = workbook.getSheetAt(v);
            int rowCount = sheet.getLastRowNum();
            int colCount = sheet.getRow(0).getLastCellNum();


            for (int i = 0; i < rowCount; i++) {
                XSSFRow currentRow = sheet.getRow(i);

                for (int j = 0; j < colCount; j++) {
                    String currentCell = currentRow.getCell(j).toString();
                    System.out.print("   " + currentCell + "||");
                }
                System.out.println();
            }
            System.out.println("------------");
        }
        System.out.println();
        System.out.println("-----------------------------------------------------");



        /* int deg = 0;
        while(deg<rowCount)
        {
            XSSFRow currentRow = sheet.getRow(deg);

            String b_type = currentRow.getCell(7).toString();
            if(b_type.equals("A(+)") || b_type.equals("A(-)"))
            {
                System.out.println(currentRow.getCell(1).toString() + " " + currentRow.getCell(2).toString()
                + ": " + b_type);
            }

            deg++;
        } */




        Scanner input = new Scanner(System.in);

        System.out.print("Listelenmesini istediğiniz kan  grubu: ");
        String bloodType = input.nextLine();
        ArrayList list3 = new ArrayList();
        ArrayList list4 = new ArrayList();
        for(int v=0; v<workbook.getNumberOfSheets(); v++)
        {
            XSSFSheet sheet = workbook.getSheetAt(v);
            int rowCount = sheet.getLastRowNum();
            int colCount = sheet.getRow(0).getLastCellNum();

            int deg = 0;
            while (deg < rowCount) {
                XSSFRow currentRow = sheet.getRow(deg);

                String b_type = currentRow.getCell(8).toString();
                if (b_type.equals(bloodType)) {
                    String idList = currentRow.getCell(0).toString();
                    list3.add(idList);
                    //System.out.println(currentRow.getCell(1).toString() + " " + currentRow.getCell(2).toString()
                    //        + ": " + b_type);
                }

                deg++;
            }
        }

        for(int i=0; i<list3.size()-1; i++)
        {
            for(int j=i+1; j<list3.size(); j++)
            {
                if(list3.get(i).equals(list3.get(j)))
                {
                    list3.remove(j);
                }
            }
        }

        for(int k=0; k<list3.size(); k++)
        {
            for(int v=0; v<workbook.getNumberOfSheets(); v++)
            {
                XSSFSheet sheet = workbook.getSheetAt(v);

                for(int i=0; i<sheet.getLastRowNum(); i++)
                {
                    XSSFRow bloodRow = sheet.getRow(i);

                    if(list3.get(k).equals(bloodRow.getCell(0).toString()))
                    {
                        list4.add(bloodRow.getCell(1) + " " + bloodRow.getCell(2) + " ====> " + bloodRow.getCell(8));
                    }
                }
            }
        }
        for(int i=0; i<list4.size()-1; i++)
        {
            for(int j=i+1; j<list4.size(); j++)
            {
                if(list4.get(i).equals(list4.get(j)))
                {
                    list4.remove(j);
                }
            }
        }
        list4.forEach((n) -> System.out.println(n));


        XSSFSheet sheet = workbook.getSheetAt(0);
        int rowCount = sheet.getLastRowNum();
        int colCount = sheet.getRow(0).getLastCellNum();

        ArrayList<String> list = new ArrayList();
        for(int x=0; x<rowCount; x++)
        {
            XSSFRow currentRow = sheet.getRow(x);

            for(int i=x; i<rowCount; i++)
            {
                String name = currentRow.getCell(1).toString();
                XSSFRow changeRow = sheet.getRow(i+1);
                String fthr_name = changeRow.getCell(7).toString();

                if(name.equals(fthr_name))
                {
                    if(currentRow.getCell(9).toString().equals(changeRow.getCell(9).toString()))
                    {
                        list.add(currentRow.getCell(0).toString());
                        list.add(changeRow.getCell(0).toString());
                    }
                }
            }
        }

        for(int i=0; i<list.size()-1; i++)
        {
            for(int j=i+1; j<list.size(); j++)
            {
                if(list.get(i).equals(list.get(j)))
                {
                    list.remove(j);
                }
            }
        }



        ArrayList<String> list2 = new ArrayList();

        for(int k=0; k<list.size(); k++)
        {
            int deg2 = 0;

            while(deg2<rowCount)
            {
                XSSFRow jobRow = sheet.getRow(deg2);
                String changed;

                if(list.get(k).equals(jobRow.getCell(0).toString()))
                {
                    String both = jobRow.getCell(1).toString().concat(" " + jobRow.getCell(2).toString() + " ===> " + jobRow.getCell(9).toString());
                    list2.add(both);
                }

                deg2++;
            }
        }
        System.out.print("\n----Babadan oğula aynı mesleği yapan kişiler----\n");
        list2.forEach((n) -> System.out.println(n));


    }
}