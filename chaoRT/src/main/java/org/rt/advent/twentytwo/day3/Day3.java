package org.rt.advent.twentytwo.day3;

import org.rt.advent.util.DayPuzzle;
import org.rt.advent.util.PuzzleFailedException;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Iterator;

public class Day3 extends DayPuzzle {


    public static void main(String[] args) {
        Day3 day1 = new Day3();
        runPuzzles(day1);
    }

    @Override
    public String puzzle1() throws PuzzleFailedException {
        try {
            return ""+ RucksSacks.CalcSharedItemPriorities(getDayStreamAllLinesAsStream());
        } catch (Exception e) {
            throw new PuzzleFailedException("no result for puzzle "+ Day3.class.getSimpleName(),e);
        }

    }

    @Override
    public String puzzle2() throws PuzzleFailedException {
        try {
            Collection<String> lines = Arrays.asList(getDayStreamAllLines());
            Iterator<String> itLines = lines.iterator();
            ArrayList<ElfGroup> allGroups = new ArrayList<>();
            while (itLines.hasNext()) {
                allGroups.add(ElfGroup.createFrom(itLines));
            }

            return ""+allGroups.stream().mapToInt(ElfGroup::FindCommonCharPriority).sum();
        } catch (Exception e) {
            throw new PuzzleFailedException("no result for puzzle "+ Day3.class.getSimpleName(),e);
        }
    }
}
