package org.rt.advent.twentytwo.day1;

import org.rt.advent.util.DayPuzzle;
import org.rt.advent.util.PuzzleFailedException;

import java.util.List;

public class Day1 extends DayPuzzle {


    public static void main(String[] args) {
        Day1 day1 = new Day1();
        runPuzzles(day1);
    }

    @Override
    public String puzzle1() throws PuzzleFailedException {
        try {
            List<Elf> elfs = Elf.ParseSnacks(getDayStream());
            return ""+Elf.getMax(elfs);
        } catch (Exception e) {
            throw new PuzzleFailedException("no result for puzzle "+ Day1.class.getSimpleName(),e);
        }

    }

    @Override
    public String puzzle2() throws PuzzleFailedException {
        try {
            List<Elf> elfs = Elf.ParseSnacks(getDayStream());
            return ""+Elf.getTopThreeMaxSum(elfs);
        } catch (Exception e) {
            throw new PuzzleFailedException("no result for puzzle "+ Day1.class.getSimpleName(),e);
        }
    }
}
