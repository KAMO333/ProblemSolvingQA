public class JedliksToyCar {
    public int driven;
    public int battery;

    public JedliksToyCar() {
        this.driven = 0;
        this.battery = 100;
    }

    public static JedliksToyCar buy() {
        return new JedliksToyCar();
    }

    public String distanceDisplay() {
        return "Driven " + this.driven + " meters";
    }

    public String batteryDisplay() {
        return this.battery > 0 ? "Battery at " + this.battery + "%" : "Battery empty";
    }

    public void drive() {
        this.driven += 20;
        this.battery -= 1;
    }
}
