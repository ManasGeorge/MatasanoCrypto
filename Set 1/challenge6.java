import java.util.Base64;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;
import java.lang.Integer;
import java.lang.Byte;
import java.lang.Double;
import java.util.Arrays;

public class challenge6 {
    public static void main (String[] args) {
        Path file = Paths.get ("6.txt");
        //Mime, otherwise newlines screw things up
        Base64.Decoder dec = Base64.getMimeDecoder();
        try {
            byte[] fileContents = Files.readAllBytes (file);
            byte[] ciphertext = dec.decode (fileContents);
            int keyLen = findKeyLen (ciphertext);
            byte[][] blocks = new byte[keyLen][ciphertext.length / keyLen];
            for (int j = 0; j < keyLen; j++) {
                for (int i = 0 ; i < ciphertext.length / keyLen; i ++) {
                    blocks[j][i] = ciphertext[i * keyLen + j];
                }
            }
            byte[] key = new byte[keyLen];
            for (int i = 0; i < keyLen; i++) {
                key[i] = findKey (blocks[i]);
            }
            String temp = new String (key);
            System.out.println (temp);
            byte[] plainText = new byte[ciphertext.length];
            int j = 0;
            for (int i = 0; i < ciphertext.length; i++) {
                plainText[i] = (byte) (ciphertext[i] ^ key[j++]);
                j = j % keyLen;
            }
            temp = new String (plainText);
            // System.out.println (temp);
        } catch (IOException ie) {
            System.err.println ("Could not open file");
        }
    }

    public static byte findKey (byte[] ciphertext) {
        for (byte key = 0; key != -1; key++) {
            // System.out.print (key + " ");
            byte[] possiblePlain = new byte[ciphertext.length];
            for (int i = 0; i < ciphertext.length; i++) {
                possiblePlain[i] = (byte) (key ^ ciphertext[i]);
            }
            String temp = new String (possiblePlain);
            // System.out.println (temp);
            if (temp.matches ("[a-zA-Z0-9 `!@#$%^&*()_+=\\-\\[\\]{}\\/:;'|]+") ) {
                System.out.println (temp);
                return key;
            }
        }
        return (byte) 65;
    }

    public static int findKeyLen ( byte[] ciphertext) {
        double minScore = Double.POSITIVE_INFINITY;
        int minScoreLen = 0;
        for (int len = 2; len < 50; ++len) {
            String a = new String (Arrays.copyOfRange (ciphertext, 0, len) );
            String b = new String (Arrays.copyOfRange (ciphertext, len, 2 * len) );
            String c = new String (Arrays.copyOfRange (ciphertext, 2 * len, 3 * len) );
            String d = new String (Arrays.copyOfRange (ciphertext, 3 * len, 4 * len) );
            double score = (hamming (a, b) + hamming (b, c) + hamming (c, d)
                            + hamming (a, d) + hamming (a, c) + hamming (b, d) ) / (6 * len);
            if (score < minScore) {
                minScoreLen = len;
                minScore = score;
            }
        }
        return minScoreLen;
    }

    public static double hamming (String a, String b) {
        int[] diff = new int[a.length()];
        double distance = 0;
        for (int i = 0; i < a.length() && i < b.length(); i++) {
            diff[i] = a.charAt (i) ^ b.charAt (i);
        }
        for (int i = 0; i < diff.length; i++) {
            distance += Integer.bitCount (diff[i]);
        }
        return distance;
    }
}