package org.rt.advent.twentytwo.day4;

import org.rt.advent.util.DayPuzzle;
import org.rt.advent.util.PuzzleFailedException;

import java.util.stream.Stream;

public class Day4 extends DayPuzzle {


    public static void main(String[] args) {
        Day4 day1 = new Day4();
        runPuzzles(day1);
    }

    public static long calcOverLapSecction(Stream<String> assignementLine) {
        return assignementLine.filter(Day4::doesSectionOverlap).count();
    }

    public static boolean doesSectionOverlap(String s) {
        String[] parts= s.split(",");

        return Range.parse(parts[0]).doesOverLap(Range.parse(parts[1]));
    }

    public static boolean doesSectionOverlapAtAll(String s) {
        String[] parts= s.split(",");
        return Range.parse(parts[0]).doesOverLapAtAll(Range.parse(parts[1]));
    }

    public static long calcOverLapAtAllSecction(Stream<String> assignementLine) {
        return assignementLine.filter(Day4::doesSectionOverlapAtAll).count();
    }

    public static class Range {
        int start;
        int end;

        public Range(int start, int end) {
            this.start = start;
            this.end = end;
        }

        public boolean doesOverLap(Range another) {
            return this.contains(another) || another.contains(this);
        }
        private boolean contains(Range another) {
            return Integer.compare(this.start, another.start) <= 0
                    && Integer.compare(this.end,another.end) >= 0;
        }


        public static Range parse(String value) {
            String[] parts = value.split("-");
            return new Range(Integer.valueOf(parts[0]),Integer.valueOf(parts[1]));
        }

        public boolean doesOverLapAtAll(Range another) {
            return !(this.isAfter(another) || another.isAfter(this));
        }
        boolean isAfter(Range other) {
            return this.start>other.end;
        }

    }

    @Override
    public String puzzle1() throws PuzzleFailedException {
        try {
            return ""+Day4.calcOverLapSecction(getDayStreamAllLinesAsStream());
        } catch (Exception e) {
            throw new PuzzleFailedException("no result for puzzle "+ Day4.class.getSimpleName(),e);
        }

    }

    @Override
    public String puzzle2() throws PuzzleFailedException {
        try {
            return ""+calcOverLapAtAllSecction(getDayStreamAllLinesAsStream());
        } catch (Exception e) {
            throw new PuzzleFailedException("no result for puzzle "+ Day4.class.getSimpleName(),e);
        }
    }
}
