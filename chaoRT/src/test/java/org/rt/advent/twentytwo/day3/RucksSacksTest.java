package org.rt.advent.twentytwo.day3;

import org.junit.jupiter.api.Test;
import org.rt.advent.twentytwo.utils.StringUtils;

import static org.junit.jupiter.api.Assertions.*;

class RucksSacksTest {

    @Test
    void TestSplitListInTwo() {
        assertEquals("r", RucksSacks.getLeftPart("rV"));
        assertEquals("V", RucksSacks.getRightPart("rV"));
        assertEquals("rV", RucksSacks.getLeftPart("rVnR"));
        assertEquals("nR", RucksSacks.getRightPart("rVnR"));

    }

    @Test
    void                                                                                    createFromStringMinimal() {
        RucksSacks test = RucksSacks.CreateFromString("vJ");
    }
    @Test
    void createFromString() {
        RucksSacks test = RucksSacks.CreateFromString("vJrwpWtwJgWrhcsFMMfFFhFp");
    }
    @Test
    void chekSampleOne() {
        RucksSacks test = RucksSacks.CreateFromString("vJrwpWtwJgWrhcsFMMfFFhFp");
        assertEquals('p', test.getDuplicatedElement());
    }
    static String SampleOne="vJrwpWtwJgWrhcsFMMfFFhFp\n" +
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n" +
            "PmmdzqPrVvPwwTWBwg\n" +
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n" +
            "ttgJtRGJQctTZtZT\n" +
            "CrZsJsPPZsGzwwsLwLmpwMDw";
    @Test
    void check_sample_one() {
        assertEquals(157, RucksSacks.CalcSharedItemPriorities(StringUtils.streamAsLines(SampleOne)));
    }
}