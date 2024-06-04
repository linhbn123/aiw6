package util.math.inference;

public class ArrayUtils {

    public static double average(int[] numbers) {
        if (numbers == null) {
            throw new IllegalArgumentException("Input array cannot be null.");
        }
        if (numbers.length == 0) {
            throw new IllegalArgumentException("Input array cannot be empty.");
        }
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        return (double) sum / numbers.length;
    }
}
