import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Vector;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.TreeSet;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.TreeMap;
public class CollectionExample {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        list.add("Cherry");
        for (String fruit : list) {
            System.out.println(fruit);
        }
        list.remove("Banana");
        System.out.println("Updated list: " + list);
    }
}
