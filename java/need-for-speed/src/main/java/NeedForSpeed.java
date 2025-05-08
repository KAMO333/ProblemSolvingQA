class NeedForSpeed {
    private int speed;
    private int batteryDrain;
    private int driven;
    private int battery;


    public NeedForSpeed(int speed, int batteryDrain) {
        this.speed = speed;
        this.batteryDrain = batteryDrain;
        this.driven = 0;
        this.battery = 100;
    }

    public boolean batteryDrained() {
        throw new UnsupportedOperationException("Please implement the NeedForSpeed.batteryDrained() method");
    }

    public int distanceDriven() {
        return driven;
    }

    public void drive(){
        if(battery != 0) {
            driven += speed;
            battery -= batteryDrain;
        }

    }

    public static NeedForSpeed nitro() {
        throw new UnsupportedOperationException("Please implement the (static) NeedForSpeed.nitro() method");
    }
}

class RaceTrack {
    private int distance;


    public RaceTrack(int distance) {
        this.distance = 800;
    }

    public boolean canFinishRace(NeedForSpeed car) {
        throw new UnsupportedOperationException("Please implement the RaceTrack.canFinishRace() method");
    }
}
