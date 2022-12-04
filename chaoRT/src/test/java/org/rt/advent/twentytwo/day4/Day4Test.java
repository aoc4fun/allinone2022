package org.rt.advent.twentytwo.day4;

import org.junit.jupiter.api.Test;
import org.rt.advent.twentytwo.utils.StringUtils;

import static org.junit.jupiter.api.Assertions.*;

class Day4Test {
    static String sample1="2-4,6-8\n" +
            "2-3,4-5\n" +
            "5-7,7-9\n" +
            "2-8,3-7\n" +
            "6-6,4-6\n" +
            "2-6,4-8";
    @Test
    void SampleOneTest() {
        assertEquals(2, Day4.calcOverLapSecction(StringUtils.streamAsLines(sample1)));
    }
    @Test
    void SampleOneTestOverlapAtAll() {
        assertEquals(4, Day4.calcOverLapAtAllSecction(StringUtils.streamAsLines(sample1)));
    }
    @Test
    void TestSampleOverLap() {
        assertEquals(true, Day4.doesSectionOverlap("2-8,3-7"));
    }

    @Test
    void TestSampleOverLapAtAll() {
        assertEquals(true, Day4.doesSectionOverlapAtAll("2-8,3-10"));
        assertEquals(true, Day4.doesSectionOverlapAtAll("2-8,8-10"));
        assertEquals(false, Day4.doesSectionOverlapAtAll("2-8,9-10"));

    }
}