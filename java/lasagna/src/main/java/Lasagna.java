public class Lasagna {
    int minutesInOven = 40;

    public  int expectedMinutesInOven() {
        return minutesInOven;
    }

    public int remainingMinutesInOven(int minutesSpend) {
        return expectedMinutesInOven() - minutesSpend;
    }

    public int preparationTimeInMinutes(int layers) {
        return layers * 2;
    }

    public int totalTimeInMinutes(int layers, int minutesInOven) {
        return preparationTimeInMinutes(layers) + minutesInOven ;
    }

}
