public class LogLevels {
    public static String message(String logline) {
        String[] arr = logline.split(":");
        return arr[1].trim();
    }

    public static String logLevel(String logLine) {
        String[] arr = logLine.split(":");
        return arr[0].toLowerCase().replaceAll("[^a-zA-Z]", "");

    }

    public static String reformat(String logLine) {
        return  message(logLine) + " " + "(" + logLevel(logLine) + ")";
    }
}
