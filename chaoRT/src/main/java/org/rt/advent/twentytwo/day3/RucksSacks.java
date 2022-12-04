package org.rt.advent.twentytwo.day3;

import java.util.stream.Stream;

public class RucksSacks {
    Compartment leftCompartment;
    Compartment rightCompartment;

    Compartment merge;

    private RucksSacks(String packageList) {
        leftCompartment=Compartment.createFromString(getLeftPart(packageList));
        rightCompartment=Compartment.createFromString(getRightPart(packageList));
        merge=Compartment.createFromString(packageList);
    }
    public static RucksSacks CreateFromString(String packageList) {
        if(packageList.length()%2 !=0) throw new IllegalArgumentException("packageList length should split in two");
        return new RucksSacks(packageList);
    }

    public static int CalcSharedItemPriorities(Stream<String> stacks) {
        return stacks.map(RucksSacks::CreateFromString)
                .mapToInt(RucksSacks::getDuplicatedElementPriority)
                .sum();
    }

    public char getDuplicatedElement() {
        return leftCompartment.getCommonItemWith(rightCompartment);
    }
    public int getDuplicatedElementPriority() {
        return Compartment.getCharValue(leftCompartment.getCommonItemWith(rightCompartment));
    }
    static String getLeftPart(String packageList) {
        return packageList.subSequence(0, packageList.length()/2).toString();
    }
    static String getRightPart(String packageList) {
        return packageList.subSequence(packageList.length()/2, packageList.length()).toString();
    }
}
