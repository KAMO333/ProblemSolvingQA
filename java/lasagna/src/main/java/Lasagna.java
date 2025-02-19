public class Lasagna {
    // TODO: define the 'expectedMinutesInOven()' method
    int minutesInOven = 40;

    public  int expectedMinutesInOven() {
        return minutesInOven;
    }

    // TODO: define the 'remainingMinutesInOven()' method
    public int remainingMinutesInOven(int minutesSpend) {
        return minutesInOven - minutesSpend;
    }

    // TODO: define the 'preparationTimeInMinutes()' method
    public int preparationTimeInMinutes(int layers) {
        return layers * 2;
    }

    // TODO: define the 'totalTimeInMinutes()' method
    public int totalTimeInMinutes(int layers, int minutesInOven) {
        return preparationTimeInMinutes(layers) + minutesInOven ;
    }

}
