package org.rt.advent.twentytwo.utils;

import java.io.BufferedReader;
import java.io.StringReader;
import java.util.stream.Stream;

public class StringUtils {
    public static Stream<String> streamAsLines(String value) {
        return new BufferedReader(new StringReader(value)).lines();
    }
}
