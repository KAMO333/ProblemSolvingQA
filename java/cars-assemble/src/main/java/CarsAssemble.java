public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        int carsPerHour = 221;

       switch (speed) {
           case 1:
               return carsPerHour;
           case 2:
               return 2 * carsPerHour;
           case 3:
               return 3 * carsPerHour;
           case 4:
               return 4 * carsPerHour;
           case 5:
               return 5 * carsPerHour;
           case 6:
               return 6 * carsPerHour;
           case 7:
               return 7 * carsPerHour;
           case 8:
               return 8 * carsPerHour;
           case 9:
               return 9 * carsPerHour;
           case 10:
               return 10 * carsPerHour;
           default:
               return 0;
       }
    }

    public int workingItemsPerMinute(int speed) {
        throw new UnsupportedOperationException("Please implement the CarsAssemble.workingItemsPerMinute() method");
    }
}
