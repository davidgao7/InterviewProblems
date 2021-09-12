import java.util.Arrays;

public class minimumLengthEncoding {
    public int minimumEncoding(String[] words) {
        // 1. sort the string arr based on length of String
        // longer string are more likely be in the encoding since
        // shorter string will be more likely included in longer string
        Arrays.sort(words, (a, b) -> b.length() - a.length());

        // 2. create a string of valid encoding
        StringBuilder encoding = new StringBuilder();

        for (String s : words) {
            if (encoding.indexOf(s + "#") == -1) { // check string + # appears in the encoding or not(-1)
                encoding.append(s).append("#"); // if not , add
            }
        }
        return encoding.length();
    }
}
