package org.rt.advent.twentytwo.day2;

import org.rt.advent.util.DayPuzzle;
import org.rt.advent.util.PuzzleFailedException;

public class Day2 extends DayPuzzle {


    public static void main(String[] args) {
        Day2 day1 = new Day2();
        runPuzzles(day1);
    }

    @Override
    public String puzzle1() throws PuzzleFailedException {
        try {
            return ""+RPCGame.ParseAllAndGetScoreOfPlayer2(this.getDayStreamAllLinesAsStream());
        } catch (Exception e) {
            throw new PuzzleFailedException("no result for puzzle "+ Day2.class.getSimpleName(),e);
        }

    }

    @Override
    public String puzzle2() throws PuzzleFailedException {
        try {
            return ""+RPCGameDecoded.ParseAllAndGetScoreOfPlayer2(this.getDayStreamAllLinesAsStream());
        } catch (Exception e) {
            throw new PuzzleFailedException("no result for puzzle "+ Day2.class.getSimpleName(),e);
        }
    }
}
