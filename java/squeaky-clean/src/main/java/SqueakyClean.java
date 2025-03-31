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

        StringBuilder newResults = new StringBuilder();

        for (int j = 0; j < results.length(); j++) {
            if (results.charAt(j) == '4') {
                newResults.append('a');
            } else if (results.charAt(j) == '3') {
                newResults.append('e');
            } else if (results.charAt(j) == '0') {
                newResults.append('o');
            } else if (results.charAt(j) == '1') {
                newResults.append('l');
            } else if (results.charAt(j) == '7') {
                newResults.append('t');
            } else {
                newResults.append(results.charAt(j));
            }

        }
        return newResults.toString();
    }
}
