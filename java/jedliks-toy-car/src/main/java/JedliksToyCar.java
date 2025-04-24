public class JedliksToyCar {
    public int driven;
    public String battery = "Battery at 100%";

    public JedliksToyCar() {
        this.driven = 0;
    }

    public static JedliksToyCar buy() {
        return new JedliksToyCar();
    }

    public String distanceDisplay() {
        return "Driven " + this.driven + " meters";
    }

    public String batteryDisplay() {
        JedliksToyCar car1 = new JedliksToyCar();
        return car1.battery;
    }

    public void drive() {
        this.driven += 20;
    }
}
