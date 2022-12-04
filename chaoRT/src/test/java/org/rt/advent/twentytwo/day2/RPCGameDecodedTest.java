package org.rt.advent.twentytwo.day2;

import org.junit.Test;
import org.rt.advent.twentytwo.utils.StringUtils;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class RPCGameDecodedTest {
    @Test
    public void sould_parse_one_game() {
        assertEquals(4, RPCGameDecoded.getScoreOfPlayer2("A Y"));
    }
    @Test
    public void when_eval_game_of_sample_one_then_score_should_match() {
        assertEquals(4, RPCGameDecoded.getScoreOfPlayer2("A Y"));
        assertEquals(1, RPCGameDecoded.getScoreOfPlayer2("B X"));
        assertEquals(7, RPCGameDecoded.getScoreOfPlayer2("C Z"));

    }
    @Test
    public void when_eval_sample_game_then_score_should_match() {
        String sampleGame="A Y\n" +
                "B X\n" +
                "C Z";
        assertEquals(12, RPCGameDecoded.ParseAllAndGetScoreOfPlayer2(StringUtils.streamAsLines(sampleGame)));
    }


}