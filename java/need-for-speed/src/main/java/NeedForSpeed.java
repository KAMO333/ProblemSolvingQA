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
        if (battery == 100 || battery >= batteryDrain) {
            return false;
        } else  {
            return true;
        }
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
       return new NeedForSpeed(50, 4);
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
