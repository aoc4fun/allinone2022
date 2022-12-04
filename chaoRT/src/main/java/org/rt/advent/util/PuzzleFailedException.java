package org.rt.advent.util;

public class PuzzleFailedException extends Exception {
    public PuzzleFailedException(String s, Exception e) {
        super(s,e);
    }
}
