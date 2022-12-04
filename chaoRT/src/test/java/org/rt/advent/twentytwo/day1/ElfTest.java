package org.rt.advent.twentytwo.day1;

import org.junit.Test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.StringReader;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class ElfTest {
    static String sample="1000\n" +
            "2000\n" +
            "3000\n" +
            "\n" +
            "4000\n" +
            "\n" +
            "5000\n" +
            "6000\n" +
            "\n" +
            "7000\n" +
            "8000\n" +
            "9000\n" +
            "\n" +
            "10000";
    @Test
    public void sample_should_match() throws IOException {

        List<Elf> myElfs = Elf.ParseSnacks(new BufferedReader(new StringReader(sample)));
        assertEquals(24000, Elf.getMax(myElfs));
    }
    @Test
    public void sample2_should_match() throws IOException {

        List<Elf> myElfs = Elf.ParseSnacks(new BufferedReader(new StringReader(sample)));
        assertEquals(45000, Elf.getTopThreeMaxSum(myElfs));
    }

}