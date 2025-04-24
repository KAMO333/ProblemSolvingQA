public class JedliksToyCar {
    public String driven = "Driven 0 meters";
    public String battery = "Battery at 100%";

    public static JedliksToyCar buy() {
        return new JedliksToyCar();
    }

    public String distanceDisplay() {
        JedliksToyCar car = new JedliksToyCar();
        return car.driven;
    }

    public String batteryDisplay() {
        JedliksToyCar car1 = new JedliksToyCar();
        return car1.battery;
    }

    public void drive() {
        throw new UnsupportedOperationException("Please implement the JedliksToyCar.drive()  method");
    }
}
