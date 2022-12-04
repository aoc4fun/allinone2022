package org.rt.advent.twentytwo.day1;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Elf implements Comparable<Elf> {
    List<Integer> snacks=new ArrayList<>();
    int total=0;

    private Elf() {}

    public void addSnack(Integer value) {
        snacks.add(value);
        total+=value;
    }

    public int getTotal(){
        return this.total;
    }

    private static Elf createNewAndAdd(List<Elf> currentList) {
        Elf result = new Elf();
        currentList.add(result);
        return result;
    }
    public static List<Elf> ParseSnacks(BufferedReader reader) throws IOException {
        List<Elf> result = new ArrayList<>();
        Elf last = createNewAndAdd(result);
        for(String next = reader.readLine();next!=null;next= reader.readLine()) {
            if(next.isEmpty()) {
                last = createNewAndAdd(result);
            } else {
                last.addSnack(Integer.parseInt(next));
            }
        }
        return result;
    }

    public static Integer getMax(List<Elf> someElf) {
        return someElf.stream().mapToInt(e -> e.getTotal()).max().orElseThrow();
    }

    public static Integer getTopThreeMaxSum(List<Elf> someElf) {
        return someElf.stream().sorted().limit(3).mapToInt(e->e.getTotal()).sum();
    }

    @Override
    public int compareTo(Elf o) {
        return -Integer.compare(this.getTotal(), o.getTotal());
    }
}
