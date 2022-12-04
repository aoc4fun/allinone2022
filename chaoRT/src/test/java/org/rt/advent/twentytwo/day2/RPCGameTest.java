package org.rt.advent.twentytwo.day2;

import org.junit.Test;
import org.rt.advent.twentytwo.utils.StringUtils;

import static org.junit.jupiter.api.Assertions.*;

public class RPCGameTest {
    @Test
    public void sould_parse_one_game() {
        assertEquals(8, RPCGame.getScoreOfPlayer2("A Y"));
    }
    @Test
    public void when_eval_game_of_sample_one_then_score_should_match() {
        assertEquals(8, RPCGame.getScoreOfPlayer2("A Y"));
        assertEquals(1, RPCGame.getScoreOfPlayer2("B X"));
        assertEquals(6, RPCGame.getScoreOfPlayer2("C Z"));

    }
    @Test
    public void when_eval_sample_game_then_score_should_match() {
        String sampleGame="A Y\n" +
                "B X\n" +
                "C Z";
        assertEquals(15, RPCGame.ParseAllAndGetScoreOfPlayer2(StringUtils.streamAsLines(sampleGame)));
    }


}