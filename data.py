training_data= [
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.training;\n\npublic class ArrayUtils1 {\n\n    public static double standardDeviation(int[] numbers) {\n        if (numbers == null) {\n            throw new IllegalArgumentException(\"Input array cannot be null.\");\n        }\n        if (numbers.length == 0) {\n            throw new IllegalArgumentException(\"Input array cannot be empty.\");\n        }\n        double mean = 0;\n        for (int number : numbers) {\n            mean += number;\n        }\n        mean /= numbers.length;\n\n        double variance = 0;\n        for (int number : numbers) {\n            variance += Math.pow(number - mean, 2);\n        }\n        variance /= numbers.length;\n\n        return Math.sqrt(variance);\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.training;\n\nimport static org.junit.jupiter.api.Assertions.assertEquals;\nimport static org.junit.jupiter.api.Assertions.assertThrows;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass ArrayUtils1Test {\n\n    @Nested\n    class StandardDeviation {\n\n        @Test\n        void standardDeviationOfPositiveNumbers() {\n            assertEquals(1.4142, ArrayUtils1.standardDeviation(new int[]{1, 2, 3, 4, 5}), 0.0001);\n        }\n\n        @Test\n        void standardDeviationOfNegativeNumbers() {\n            assertEquals(1.4142, ArrayUtils1.standardDeviation(new int[]{-1, -2, -3, -4, -5}), 0.0001);\n        }\n\n        @Test\n        void standardDeviationOfMixedNumbers() {\n            assertEquals(2.1602, ArrayUtils1.standardDeviation(new int[]{1, -1, 2, -2, 3, -3}), 0.0001);\n        }\n\n        @Test\n        void standardDeviationOfSingleElementArray() {\n            assertEquals(0.0, ArrayUtils1.standardDeviation(new int[]{42}), 0.0001);\n        }\n\n        @Test\n        void standardDeviationOfNullArray() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                ArrayUtils1.standardDeviation(null);\n            });\n            assertEquals(\"Input array cannot be null.\", exception.getMessage());\n        }\n\n        @Test\n        void standardDeviationOfEmptyArray() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                ArrayUtils1.standardDeviation(new int[]{});\n            });\n            assertEquals(\"Input array cannot be empty.\", exception.getMessage());\n        }\n    }\n}\n```"
            }
        ]
    },
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.training;\n\npublic class ArrayUtils2 {\n\n    public static double variance(int[] numbers) {\n        if (numbers == null) {\n            throw new IllegalArgumentException(\"Input array cannot be null.\");\n        }\n        if (numbers.length == 0) {\n            throw new IllegalArgumentException(\"Input array cannot be empty.\");\n        }\n        double mean = 0;\n        for (int number : numbers) {\n            mean += number;\n        }\n        mean /= numbers.length;\n\n        double variance = 0;\n        for (int number : numbers) {\n            variance += Math.pow(number - mean, 2);\n        }\n        variance /= numbers.length;\n\n        return variance;\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.training;\n\nimport static org.junit.jupiter.api.Assertions.assertEquals;\nimport static org.junit.jupiter.api.Assertions.assertThrows;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass ArrayUtils2Test {\n\n    @Nested\n    class Variation {\n\n        @Test\n        void varianceOfPositiveNumbers() {\n            assertEquals(2.0, ArrayUtils2.variance(new int[]{1, 2, 3, 4, 5}), 0.0001);\n        }\n\n        @Test\n        void varianceOfNegativeNumbers() {\n            assertEquals(2.0, ArrayUtils2.variance(new int[]{-1, -2, -3, -4, -5}), 0.0001);\n        }\n\n        @Test\n        void varianceOfMixedNumbers() {\n            assertEquals(4.6667, ArrayUtils2.variance(new int[]{1, -1, 2, -2, 3, -3}), 0.0001);\n        }\n\n        @Test\n        void varianceOfSingleElementArray() {\n            assertEquals(0.0, ArrayUtils2.variance(new int[]{42}), 0.0001);\n        }\n\n        @Test\n        void varianceOfNullArray() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                ArrayUtils2.variance(null);\n            });\n            assertEquals(\"Input array cannot be null.\", exception.getMessage());\n        }\n\n        @Test\n        void varianceOfEmptyArray() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                ArrayUtils2.variance(new int[]{});\n            });\n            assertEquals(\"Input array cannot be empty.\", exception.getMessage());\n        }\n    }\n}\n```"
            }
        ]
    },
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.training;\n\npublic class ArrayUtils3 {\n\n    public static int[] reverse(int[] numbers) {\n        if (numbers == null) {\n            throw new IllegalArgumentException(\"Input array cannot be null.\");\n        }\n        int length = numbers.length;\n        int[] reversed = new int[length];\n        for (int i = 0; i < length; i++) {\n            reversed[i] = numbers[length - 1 - i];\n        }\n        return reversed;\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.training;\n\nimport static org.junit.jupiter.api.Assertions.assertArrayEquals;\nimport static org.junit.jupiter.api.Assertions.assertEquals;\nimport static org.junit.jupiter.api.Assertions.assertThrows;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass ArrayUtils3Test {\n\n    @Nested\n    class Reverse {\n\n        @Test\n        void reverseOfPositiveNumbers() {\n            assertArrayEquals(new int[]{5, 4, 3, 2, 1}, ArrayUtils3.reverse(new int[]{1, 2, 3, 4, 5}));\n        }\n\n        @Test\n        void reverseOfNegativeNumbers() {\n            assertArrayEquals(new int[]{-5, -4, -3, -2, -1}, ArrayUtils3.reverse(new int[]{-1, -2, -3, -4, -5}));\n        }\n\n        @Test\n        void reverseOfMixedNumbers() {\n            assertArrayEquals(new int[]{3, -2, 1}, ArrayUtils3.reverse(new int[]{1, -2, 3}));\n        }\n\n        @Test\n        void reverseOfSingleElementArray() {\n            assertArrayEquals(new int[]{42}, ArrayUtils3.reverse(new int[]{42}));\n        }\n\n        @Test\n        void reverseOfEmptyArray() {\n            assertArrayEquals(new int[]{}, ArrayUtils3.reverse(new int[]{}));\n        }\n\n        @Test\n        void reverseOfNullArray() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                ArrayUtils3.reverse(null);\n            });\n            assertEquals(\"Input array cannot be null.\", exception.getMessage());\n        }\n    }\n}\n```"
            }
        ]
    },
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.training;\n\npublic class ArrayUtils4 {\n\n    public static int max(int[] numbers) {\n        if (numbers == null) {\n            throw new IllegalArgumentException(\"Input array cannot be null.\");\n        }\n        if (numbers.length == 0) {\n            throw new IllegalArgumentException(\"Input array cannot be empty.\");\n        }\n        int max = numbers[0];\n        for (int number : numbers) {\n            if (number > max) {\n                max = number;\n            }\n        }\n        return max;\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.training;\n\nimport static org.junit.jupiter.api.Assertions.assertEquals;\nimport static org.junit.jupiter.api.Assertions.assertThrows;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass ArrayUtils4Test {\n\n    @Nested\n    class Max {\n\n        @Test\n        void maxOfPositiveNumbers() {\n            assertEquals(5, ArrayUtils4.max(new int[]{1, 2, 3, 4, 5}));\n        }\n\n        @Test\n        void maxOfNegativeNumbers() {\n            assertEquals(-1, ArrayUtils4.max(new int[]{-1, -2, -3, -4, -5}));\n        }\n\n        @Test\n        void maxOfMixedNumbers() {\n            assertEquals(3, ArrayUtils4.max(new int[]{1, -2, 3}));\n        }\n\n        @Test\n        void maxOfSingleElementArray() {\n            assertEquals(42, ArrayUtils4.max(new int[]{42}));\n        }\n\n        @Test\n        void maxOfNullArray() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                ArrayUtils4.max(null);\n            });\n            assertEquals(\"Input array cannot be null.\", exception.getMessage());\n        }\n\n        @Test\n        void maxOfEmptyArray() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                ArrayUtils4.max(new int[]{});\n            });\n            assertEquals(\"Input array cannot be empty.\", exception.getMessage());\n        }\n    }\n}\n```"
            }
        ]
    },
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.training;\n\npublic class ArrayUtils5 {\n\n    public static int min(int[] numbers) {\n        if (numbers == null) {\n            throw new IllegalArgumentException(\"Input array cannot be null.\");\n        }\n        if (numbers.length == 0) {\n            throw new IllegalArgumentException(\"Input array cannot be empty.\");\n        }\n        int min = numbers[0];\n        for (int number : numbers) {\n            if (number < min) {\n                min = number;\n            }\n        }\n        return min;\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.training;\n\nimport static org.junit.jupiter.api.Assertions.assertEquals;\nimport static org.junit.jupiter.api.Assertions.assertThrows;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass ArrayUtils5Test {\n\n    @Nested\n    class Min {\n\n        @Test\n        void minOfPositiveNumbers() {\n            assertEquals(1, ArrayUtils5.min(new int[]{1, 2, 3, 4, 5}));\n        }\n\n        @Test\n        void minOfNegativeNumbers() {\n            assertEquals(-5, ArrayUtils5.min(new int[]{-1, -2, -3, -4, -5}));\n        }\n\n        @Test\n        void minOfSingleElementArray() {\n            assertEquals(42, ArrayUtils5.min(new int[]{42}));\n        }\n\n        @Test\n        void minOfMixedNumbers() {\n            assertEquals(-2, ArrayUtils5.min(new int[]{1, -2, 3}));\n        }\n\n        @Test\n        void minOfNullArray() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                ArrayUtils5.min(null);\n            });\n            assertEquals(\"Input array cannot be null.\", exception.getMessage());\n        }\n\n        @Test\n        void minOfEmptyArray() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                ArrayUtils5.min(new int[]{});\n            });\n            assertEquals(\"Input array cannot be empty.\", exception.getMessage());\n        }\n    }\n}\n```"
            }
        ]
    },
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.training;\n\npublic class Calculator {\n\n    public static double power(double base, double exponent) {\n        if (base == 0 && exponent <= 0) {\n            throw new IllegalArgumentException(\"0 cannot be raised to a non-positive power.\");\n        }\n        return Math.pow(base, exponent);\n    }\n\n    public static int modulo(int dividend, int divisor) {\n        if (divisor == 0) {\n            throw new IllegalArgumentException(\"Division by zero\");\n        }\n        return dividend % divisor;\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.training;\n\nimport static org.junit.jupiter.api.Assertions.assertEquals;\nimport static org.junit.jupiter.api.Assertions.assertThrows;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass CalculatorTest {\n\n    @Nested\n    class Power {\n\n        @Test\n        void positiveNumbers() {\n            assertEquals(8.0, Calculator.power(2, 3), 0.0001);\n        }\n\n        @Test\n        void negativeBase() {\n            assertEquals(-8.0, Calculator.power(-2, 3), 0.0001);\n        }\n\n        @Test\n        void zeroExponent() {\n            assertEquals(1.0, Calculator.power(2, 0), 0.0001);\n        }\n\n        @Test\n        void negativeExponent() {\n            assertEquals(0.125, Calculator.power(2, -3), 0.0001);\n        }\n\n        @Test\n        void zeroBase() {\n            assertEquals(0.0, Calculator.power(0, 3), 0.0001);\n        }\n\n        @Test\n        void zeroBaseZeroExponent() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                Calculator.power(0, 0);\n            });\n            assertEquals(\"0 cannot be raised to a non-positive power.\", exception.getMessage());\n        }\n    }\n\n    @Nested\n    class Modulo {\n\n        @Test\n        void positiveNumbers() {\n            assertEquals(1, Calculator.modulo(10, 3));\n        }\n\n        @Test\n        void negativeDividend() {\n            assertEquals(-1, Calculator.modulo(-10, 3));\n        }\n\n        @Test\n        void negativeDivisor() {\n            assertEquals(1, Calculator.modulo(10, -3));\n        }\n\n        @Test\n        void negativeNumbers() {\n            assertEquals(-1, Calculator.modulo(-10, -3));\n        }\n\n        @Test\n        void zeroDividend() {\n            assertEquals(0, Calculator.modulo(0, 3));\n        }\n\n        @Test\n        void zeroDivisor() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                Calculator.modulo(10, 0);\n            });\n            assertEquals(\"Division by zero\", exception.getMessage());\n        }\n    }\n}\n```"
            }
        ]
    },
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.training;\n\npublic class NumberUtils1 {\n\n    public static long factorial(int n) {\n        if (n < 0) {\n            throw new IllegalArgumentException(\"Factorial is not defined for negative numbers.\");\n        }\n        long result = 1;\n        for (int i = 1; i <= n; i++) {\n            result *= i;\n        }\n        return result;\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.training;\n\nimport static org.junit.jupiter.api.Assertions.assertEquals;\nimport static org.junit.jupiter.api.Assertions.assertThrows;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass NumberUtils1Test {\n\n    @Nested\n    class Factorial {\n\n        @Test\n        void factorialOfZero() {\n            assertEquals(1, NumberUtils1.factorial(0));\n        }\n\n        @Test\n        void factorialOfOne() {\n            assertEquals(1, NumberUtils1.factorial(1));\n        }\n\n        @Test\n        void factorialOfPositiveNumber() {\n            assertEquals(120, NumberUtils1.factorial(5));\n        }\n\n        @Test\n        void factorialOfLargeNumber() {\n            assertEquals(3628800, NumberUtils1.factorial(10));\n        }\n\n        @Test\n        void factorialOfNegativeNumber() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                NumberUtils1.factorial(-1);\n            });\n            assertEquals(\"Factorial is not defined for negative numbers.\",\n                    exception.getMessage());\n        }\n    }\n}\n```"
            }
        ]
    },
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.training;\n\npublic class NumberUtils2 {\n\n    public static long fibonacci(int n) {\n        if (n < 0) {\n            throw new IllegalArgumentException(\"Fibonacci number is not defined for negative numbers.\");\n        }\n        if (n == 0) {\n            return 0;\n        }\n        if (n == 1) {\n            return 1;\n        }\n        long a = 0, b = 1;\n        for (int i = 2; i <= n; i++) {\n            long temp = a + b;\n            a = b;\n            b = temp;\n        }\n        return b;\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.training;\n\nimport static org.junit.jupiter.api.Assertions.assertEquals;\nimport static org.junit.jupiter.api.Assertions.assertThrows;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass NumberUtils2Test {\n\n    @Nested\n    class Fibonacci {\n\n        @Test\n        void fibonacciOfZero() {\n            assertEquals(0, NumberUtils2.fibonacci(0));\n        }\n\n        @Test\n        void fibonacciOfOne() {\n            assertEquals(1, NumberUtils2.fibonacci(1));\n        }\n\n        @Test\n        void fibonacciOfPositiveNumber() {\n            assertEquals(5, NumberUtils2.fibonacci(5));\n        }\n\n        @Test\n        void fibonacciOfLargeNumber() {\n            assertEquals(55, NumberUtils2.fibonacci(10));\n        }\n\n        @Test\n        void fibonacciOfNegativeNumber() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                NumberUtils2.fibonacci(-1);\n            });\n            assertEquals(\"Fibonacci number is not defined for negative numbers.\", exception.getMessage());\n        }\n    }\n}\n```"
            }
        ]
    },
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.training;\n\npublic class NumberUtils3 {\n\n    public static boolean isPrime(int n) {\n        if (n <= 1) {\n            return false;\n        }\n        if (n <= 3) {\n            return true;\n        }\n        if (n % 2 == 0 || n % 3 == 0) {\n            return false;\n        }\n        for (int i = 5; i * i <= n; i += 6) {\n            if (n % i == 0 || n % (i + 2) == 0) {\n                return false;\n            }\n        }\n        return true;\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.training;\n\nimport static org.junit.jupiter.api.Assertions.assertFalse;\nimport static org.junit.jupiter.api.Assertions.assertTrue;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass NumberUtils3Test {\n\n    @Nested\n    class Prime {\n\n        @Test\n        void primeNumberTwo() {\n            assertTrue(NumberUtils3.isPrime(2));\n        }\n\n        @Test\n        void primeNumberThree() {\n            assertTrue(NumberUtils3.isPrime(3));\n        }\n\n        @Test\n        void nonPrimeNumber() {\n            assertFalse(NumberUtils3.isPrime(4));\n        }\n\n        @Test\n        void largePrimeNumber() {\n            assertTrue(NumberUtils3.isPrime(29));\n        }\n\n        @Test\n        void largeNonPrimeNumber() {\n            assertFalse(NumberUtils3.isPrime(30));\n        }\n\n        @Test\n        void negativeNumber() {\n            assertFalse(NumberUtils3.isPrime(-5));\n        }\n\n        @Test\n        void zero() {\n            assertFalse(NumberUtils3.isPrime(0));\n        }\n\n        @Test\n        void one() {\n            assertFalse(NumberUtils3.isPrime(1));\n        }\n    }\n}\n```"
            }
        ]
    },
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.training;\n\npublic class NumberUtils4 {\n\n    public static boolean isPalindrome(int number) {\n        int original = number;\n        int reverse = 0;\n        while (number != 0) {\n            int digit = number % 10;\n            reverse = reverse * 10 + digit;\n            number /= 10;\n        }\n        return original == reverse;\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.training;\n\nimport static org.junit.jupiter.api.Assertions.assertFalse;\nimport static org.junit.jupiter.api.Assertions.assertTrue;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass NumberUtils4Test {\n\n    @Nested\n    class Palindrome {\n\n        @Test\n        void palindromePositiveNumber() {\n            assertTrue(NumberUtils4.isPalindrome(121));\n        }\n\n        @Test\n        void palindromeNegativeNumber() {\n            assertTrue(NumberUtils4.isPalindrome(-121));\n        }\n\n        @Test\n        void nonPalindromeNumber() {\n            assertFalse(NumberUtils4.isPalindrome(123));\n        }\n\n        @Test\n        void singleDigitPalindrome() {\n            assertTrue(NumberUtils4.isPalindrome(7));\n        }\n\n        @Test\n        void zeroPalindrome() {\n            assertTrue(NumberUtils4.isPalindrome(0));\n        }\n    }\n}\n```"
            }
        ]
    }
]

validation_data= [
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.validation;\n\npublic class BasicOperations1 {\n\n    public static int add(int a, int b) {\n        return a + b;\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.validation;\n\nimport static org.junit.jupiter.api.Assertions.assertEquals;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass BasicOperations1Test {\n\n    @Nested\n    class Add {\n\n        @Test\n        void additionOfPositiveNumbers() {\n            assertEquals(5, BasicOperations1.add(2, 3));\n        }\n\n        @Test\n        void additionOfNegativeNumbers() {\n            assertEquals(-5, BasicOperations1.add(-2, -3));\n        }\n\n        @Test\n        void additionOfMixedNumbers() {\n            assertEquals(1, BasicOperations1.add(2, -1));\n        }\n\n        @Test\n        void additionWithZero() {\n            assertEquals(3, BasicOperations1.add(3, 0));\n        }\n\n        @Test\n        void additionOfLargeNumbers() {\n            assertEquals(2000000000, BasicOperations1.add(1000000000, 1000000000));\n        }\n    }\n}\n```"
            }
        ]
    },
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.validation;\n\npublic class BasicOperations2 {\n\n    public static int subtract(int a, int b) {\n        return a - b;\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.validation;\n\nimport static org.junit.jupiter.api.Assertions.assertEquals;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass BasicOperations2Test {\n\n    @Nested\n    class Subtract {\n\n        @Test\n        void subtractionOfPositiveNumbers() {\n            assertEquals(1, BasicOperations2.subtract(3, 2));\n        }\n\n        @Test\n        void subtractionOfNegativeNumbers() {\n            assertEquals(1, BasicOperations2.subtract(-2, -3));\n        }\n\n        @Test\n        void subtractionOfMixedNumbers() {\n            assertEquals(3, BasicOperations2.subtract(2, -1));\n        }\n\n        @Test\n        void subtractionWithZero() {\n            assertEquals(3, BasicOperations2.subtract(3, 0));\n        }\n\n        @Test\n        void subtractionOfLargeNumbers() {\n            assertEquals(0, BasicOperations2.subtract(1000000000, 1000000000));\n        }\n    }\n}\n```"
            }
        ]
    },
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.validation;\n\npublic class BasicOperations3 {\n\n    public static int multiply(int a, int b) {\n        return a * b;\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.validation;\n\nimport static org.junit.jupiter.api.Assertions.assertEquals;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass BasicOperations3Test {\n\n    @Nested\n    class Multiply {\n\n        @Test\n        void multiplicationOfPositiveNumbers() {\n            assertEquals(6, BasicOperations3.multiply(2, 3));\n        }\n\n        @Test\n        void multiplicationOfNegativeNumbers() {\n            assertEquals(6, BasicOperations3.multiply(-2, -3));\n        }\n\n        @Test\n        void multiplicationOfMixedNumbers() {\n            assertEquals(-6, BasicOperations3.multiply(2, -3));\n        }\n\n        @Test\n        void multiplicationWithZero() {\n            assertEquals(0, BasicOperations3.multiply(3, 0));\n        }\n\n        @Test\n        void multiplicationOfLargeNumbers() {\n            assertEquals(100000000L, BasicOperations3.multiply(10000, 10000));\n        }\n    }\n}\n```"
            }
        ]
    },
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.validation;\n\npublic class BasicOperations4 {\n\n    public static double divide(int a, int b) {\n        if (b == 0) {\n            throw new IllegalArgumentException(\"Division by zero is not allowed.\");\n        }\n        return (double) a / b;\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.validation;\n\nimport static org.junit.jupiter.api.Assertions.assertEquals;\nimport static org.junit.jupiter.api.Assertions.assertThrows;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass BasicOperations4Test {\n\n    @Nested\n    class Divide {\n\n        @Test\n        void divisionOfPositiveNumbers() {\n            assertEquals(2.0, BasicOperations4.divide(6, 3), 0.0001);\n        }\n\n        @Test\n        void divisionOfNegativeNumbers() {\n            assertEquals(2.0, BasicOperations4.divide(-6, -3), 0.0001);\n        }\n\n        @Test\n        void divisionOfMixedNumbers() {\n            assertEquals(-2.0, BasicOperations4.divide(6, -3), 0.0001);\n        }\n\n        @Test\n        void divisionWithZeroNumerator() {\n            assertEquals(0.0, BasicOperations4.divide(0, 3), 0.0001);\n        }\n\n        @Test\n        void divisionWithZeroDenominator() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                BasicOperations4.divide(3, 0);\n            });\n            assertEquals(\"Division by zero is not allowed.\", exception.getMessage());\n        }\n\n        @Test\n        void divisionOfLargeNumbers() {\n            assertEquals(1.0, BasicOperations4.divide(1000000000, 1000000000), 0.0001);\n        }\n    }\n}\n```"
            }
        ]
    },
    {
        "messages":[
            {
                "role":"system",
                "content":"You're a java expert. You provide clear and concise answers. You do not explain, unless explicitly asked. You are excellent at generating unit tests using JUnit Jupiter to reach code coverage 100%. If the main source code has a package declaration, then the generated unit tests belong to the same package as well. You make sure unit test classes and methods are package-private instead of public."
            },
            {
                "role":"user",
                "content":"Generate unit tests for this code: \n```java\npackage util.math.validation;\n\npublic class CalendarUtils {\n\n    public static boolean isLeapYear(int year) {\n        if (year < 0) {\n            throw new IllegalArgumentException(\"Year cannot be negative.\");\n        }\n        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);\n    }\n}\n```"
            },
            {
                "role":"assistant",
                "content":"```java\npackage util.math.validation;\n\nimport static org.junit.jupiter.api.Assertions.assertEquals;\nimport static org.junit.jupiter.api.Assertions.assertFalse;\nimport static org.junit.jupiter.api.Assertions.assertThrows;\nimport static org.junit.jupiter.api.Assertions.assertTrue;\n\nimport org.junit.jupiter.api.Nested;\nimport org.junit.jupiter.api.Test;\n\nclass CalendarUtilsTest {\n\n    @Nested\n    class Leap {\n\n        @Test\n        void leapYearDivisibleBy4Not100() {\n            assertTrue(CalendarUtils.isLeapYear(2024));\n        }\n\n        @Test\n        void leapYearDivisibleBy400() {\n            assertTrue(CalendarUtils.isLeapYear(2000));\n        }\n\n        @Test\n        void nonLeapYearDivisibleBy100Not400() {\n            assertFalse(CalendarUtils.isLeapYear(1900));\n        }\n\n        @Test\n        void nonLeapYear() {\n            assertFalse(CalendarUtils.isLeapYear(2019));\n        }\n\n        @Test\n        void negativeYear() {\n            Exception exception = assertThrows(IllegalArgumentException.class, () -> {\n                CalendarUtils.isLeapYear(-1);\n            });\n            assertEquals(\"Year cannot be negative.\", exception.getMessage());\n        }\n    }\n}\n```"
            }
        ]
    }
]

