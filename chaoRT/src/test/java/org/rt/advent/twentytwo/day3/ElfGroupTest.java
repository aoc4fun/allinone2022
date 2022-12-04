package org.rt.advent.twentytwo.day3;

import org.junit.jupiter.api.Test;
import org.rt.advent.twentytwo.day1.Elf;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

class ElfGroupTest {
    @Test
    void test_sample_result() {
        ElfGroup newGroup = getElfGroupSampleOne();
        assertEquals('r' ,newGroup.FindCommonChar());
    }

    private static ElfGroup getElfGroupSampleOne() {
        ElfGroup newGroup = ElfGroup.createFromTripleString("vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg");
        return newGroup;
    }

    @Test
    void test_sample_result2() {
        ElfGroup newGroup = getElfGroupSampleTwo();
        assertEquals('Z' ,newGroup.FindCommonChar());
    }

    private static ElfGroup getElfGroupSampleTwo() {
        ElfGroup newGroup = ElfGroup.createFromTripleString("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw");
        return newGroup;
    }

    @Test
    void CheckSamplePriorities() {
        ArrayList<ElfGroup> groups = new ArrayList<>();
        groups.add(getElfGroupSampleOne());
        groups.add(getElfGroupSampleTwo());
        assertEquals(70, ElfGroup.CalcCommonCharPriorities(groups));
    }
}