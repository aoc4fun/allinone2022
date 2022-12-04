package org.rt.advent.twentytwo.day3;

import java.io.BufferedReader;
import java.util.Collection;
import java.util.Iterator;
import java.util.Set;
import java.util.TreeSet;
import java.util.stream.Stream;

public class ElfGroup {
    private Compartment elf1;
    private Compartment elf2;
    public static ElfGroup createFrom(Iterator<String> itOfString) {

        return new ElfGroup(
                Compartment.createFromString(itOfString.next()),
                Compartment.createFromString(itOfString.next()),
                Compartment.createFromString(itOfString.next())
        );
    }

    private Compartment elf3;

    public ElfGroup(Compartment elf1, Compartment elf2, Compartment elf3) {
        this.elf1 = elf1;
        this.elf2 = elf2;
        this.elf3 = elf3;
    }
    public static ElfGroup createFromTripleString(String el1, String el2, String el3) {
        return new ElfGroup(
                Compartment.createFromString(el1),
                Compartment.createFromString(el2),
                Compartment.createFromString(el3)
        );
    }

    public char FindCommonChar() {
        Set<Character> result = elf1.getCommonItemsWith(elf2);
        result.retainAll(elf3.content);
        return result.stream().findFirst().orElseThrow();
    }
    public int FindCommonCharPriority() {
        return Compartment.getCharValue(FindCommonChar());
    }


    public static int CalcCommonCharPriorities(Collection<ElfGroup> groups) {
        return groups.stream().mapToInt(ElfGroup::FindCommonCharPriority).sum();
    }
}
