public class JedliksToyCar {
    public String driven = "Driven 0 meters";

    public static JedliksToyCar buy() {
        return new JedliksToyCar();
    }

    public String distanceDisplay() {
        JedliksToyCar car = new JedliksToyCar();
        return car.driven;

    }

    public String batteryDisplay() {
        throw new UnsupportedOperationException("Please implement the JedliksToyCar.batteryDisplay()  method");
    }

    public void drive() {
        throw new UnsupportedOperationException("Please implement the JedliksToyCar.drive()  method");
    }
}
