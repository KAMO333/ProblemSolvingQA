public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        int carsPerHour = 221;

        if (speed <= 4) {
            return speed * carsPerHour;
        } else if (speed <= 8) {
            int getCarsPerHour = speed * carsPerHour;
            return getCarsPerHour * 0.9;
        } else if (speed == 9) {
            int getCarsPerHour = speed * carsPerHour;
            return getCarsPerHour * 0.8;
        } else if (speed == 10) {
            int getCarsPerHour = speed * carsPerHour;
            return getCarsPerHour * 0.77;
        } else {
            return 0.0;
        }
    }

    public int workingItemsPerMinute(int speed) {
        throw new UnsupportedOperationException("Please implement the CarsAssemble.workingItemsPerMinute() method");
    }
}
