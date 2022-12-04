package org.rt.advent.twentytwo.day3;

import org.junit.Test;

import static org.junit.jupiter.api.Assertions.*;

public class CompartmentTest {
    @Test
    public void when_getting_priorities_then_value_should_match_sample() {
        assertEquals(1,Compartment.getCharValue('a'));
        assertEquals(26,Compartment.getCharValue('z'));
        assertEquals(27,Compartment.getCharValue('A'));
        assertEquals(52,Compartment.getCharValue('Z'));

    }
    @Test
    public void given_two_compartment_with_one_item_in_common_then_should_return_the_item() {
        Compartment left = Compartment.createFromString("vJrwpWtwJgWr");
        Compartment right = Compartment.createFromString("hcsFMMfFFhFp");
        assertEquals('p', left.getCommonItemWith(right));
    }
}