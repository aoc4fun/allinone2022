package org.rt.advent.twentytwo.day2;

import java.util.stream.Stream;

public class RPCGameDecoded {
    enum Result {
        AX(4,3),
        AY(0,4),
        AZ(7,8),
        BX(8,1),
        BY(5,5),
        BZ(2,9),
        CX(3,2),
        CY(9,6),
        CZ(6,7);

        Result(int score1, int score2) {
            this.score1 = score1;
            this.score2 = score2;
        }

        int score1;
        int score2;

        public int getScore1() {
            return score1;
        }

        public int getScore2() {
            return score2;
        }

    }


    public static int getScoreOfPlayer2(String game) {
        return Result.valueOf(game.replaceAll(" ","")).getScore2();
    }
    public static int getScoreOfPlayer1(String game) {
        return ParseAndGetResult(game).getScore1();
    }

    private static Result ParseAndGetResult(String game) {
        return Result.valueOf(game.replaceAll(" ", ""));
    }

    public static int ParseAllAndGetScoreOfPlayer2(Stream<String> games) {
        return games
                .map(RPCGameDecoded::ParseAndGetResult)
                .mapToInt(Result::getScore2)
                .sum();
    }


}
