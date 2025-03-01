class SqueakyClean {
    static String clean(String identifier) {
        identifier = identifier.replaceAll(" ", "_");

        String[] parts = identifier.split("-");

        StringBuilder results = new StringBuilder(parts[0]);

        for (int i = 1; i < parts.length; i++) {
            if(!parts[i].isEmpty()) {
                results.append(parts[i].substring(0, 1).toUpperCase());
                results.append((parts[i].substring(1)));
            }
        }
        return results.toString();

    }
}
