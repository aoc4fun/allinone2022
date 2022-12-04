package org.rt.advent.twentytwo.day3;

import java.util.Arrays;
import java.util.Collections;
import java.util.Set;
import java.util.TreeSet;
import java.util.stream.Collectors;

public class Compartment {
    Set<Character> content = new TreeSet<>();
    private Compartment(String strList) {
        content = strList.chars()
                .mapToObj(e->(char)e).collect(Collectors.toSet());
    }
    public static Compartment createFromString(String contentList) {
        return new Compartment(contentList);
    }

    public Set<Character> getCommonItemsWith(Compartment other) {
        Set<Character> clone = new TreeSet<>(this.content);
        clone.retainAll(other.content);
        return clone;
    }

    static int getCharValue(Character c) {
        if(Character.isUpperCase(c)) return c.charValue()-'A'+27;
        return c.charValue()-'a'+1;
    }

    public Character getCommonItemWith(Compartment right) {
        return this.content.stream().filter(i -> right.content.contains(i)).findFirst().orElseThrow();
    }

    public int size() {
        return content.size();
    }
}
