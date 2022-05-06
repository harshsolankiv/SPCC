import java.io.*;
import java.util.*;

class exp2 {
    public static void main(String args[]) throws Exception {
        String m[] = { "L", "A", "ST" };
        String b[] = { "1001", "1011", "1111" };
        String p[] = { "DC", "EQU", "DS", "USING", "END" };
        int l[] = { 4, 1, 4 };
        int LC = 0;
        Vector<String> mneumonic = new Vector();
        Vector<String> bincode = new Vector();
        // Vector<Integer> mlength = new Vector();
        Vector<String> pseudo = new Vector();
        Vector<Integer> ppos = new Vector();
        Vector<String> symbolname = new Vector();
        Vector<Integer> symbolvalue = new Vector();
        Vector<String> format = new Vector();
        Vector<String> RA = new Vector();
        Vector<Integer> symbollength = new Vector();
        Scanner sc = new Scanner(new File("prog.txt"));
        String xx = sc.nextLine();
        StringTokenizer stt = new StringTokenizer(xx);
        Vector<String> readd = new Vector();
        while (stt.hasMoreTokens())
            readd.add(stt.nextToken());
        symbolname.add(readd.elementAt(0));
        LC = Integer.parseInt(readd.elementAt(readd.size() - 1));
        symbolvalue.add(LC);
        symbollength.add(1);
        RA.add("R");
        Vector<String> alreadyread = new Vector();
        // String prev = "";
        while (sc.hasNext()) {
            String x = sc.nextLine();
            StringTokenizer st = new StringTokenizer(x);
            Vector<String> read = new Vector();
            while (st.hasMoreTokens())
                read.add(st.nextToken());
            for (int i = 0; i < read.size(); i++) {
                int potpos = getIndex(p, read.elementAt(i));
                if (potpos == -1)
                    continue;
                pseudo.add(p[potpos]);
                ppos.add(potpos + 1);
                if (!p[potpos].equals("USING") && !p[potpos].equals("END")) {
                    symbolname.add(read.elementAt(i - 1));
                    symbollength.add(l[potpos]);
                }
            }
        }
        sc = new Scanner(new File("prog.txt"));
        String ss = sc.nextLine();
        // vishal code
        while (sc.hasNext()) {
            String x = sc.nextLine();
            StringTokenizer st = new StringTokenizer(x);
            Vector<String> read = new Vector();
            while (st.hasMoreTokens())
                read.add(st.nextToken());
            boolean flag = false;
            for (int i = 0; i < read.size(); i++) {
                int motpos = getIndex(m, read.elementAt(i));
                if (motpos != -1) {
                    mneumonic.add(m[motpos]);
                    bincode.add(b[motpos]);
                    flag = true;
                }
            }
            if (flag) {
                boolean pushed = false;
                String last = read.elementAt(read.size() - 1);
                alreadyread.add(last);
                for (int i = 0; i < symbolname.size(); i++)
                    if (symbolname.elementAt(i).equals(last)) {
                        format.add("RX");
                        pushed = true;
                        break;
                    }
                if (!pushed)
                    format.add("AX");
            }
        }
        sc = new Scanner(new File("prog.txt"));
        ss = sc.nextLine();
        while (sc.hasNext()) {
            String x = sc.nextLine();
            StringTokenizer st = new StringTokenizer(x);
            Vector<String> read = new Vector();
            while (st.hasMoreTokens())
                read.add(st.nextToken());
            for (int i = 0; i < read.size(); i++) {
                int motpos = getIndex(m, read.elementAt(i));
                if (motpos != -1) {
                    LC += 4;
                }
                int potpos = getIndex(p, read.elementAt(i));
                if (potpos != -1 && !p[potpos].equals("USING") && !p[potpos].equals("END")) {
                    symbolvalue.add(LC);
                    if (!p[potpos].equals("EQU"))
                        LC += 4;
                    continue;
                }
            }
        }
        // atharva code
        for (int i = 0; i < symbolname.size(); i++) {
            String ii = symbolname.elementAt(i);
            boolean there = false;
            for (int j = 0; j < alreadyread.size(); j++)
                if (ii.equals(alreadyread.elementAt(j))) {
                    there = true;
                    break;
                }
            RA.add(there ? "R" : "A");
        }
        System.out.println("\n------MOT------\n");
        System.out.println("Mneumonic  Binopcode  Length  Format");
        for (int i = 0; i < mneumonic.size(); i++) {
            System.out.printf("%s\t   %s\t\t%d\t%s\n", mneumonic.elementAt(i), bincode.elementAt(i), 4,
                    format.elementAt(i));
        }
        System.out.println("\n------POT------\n");
        System.out.println("Pseudo-opcode  Address");
        for (int i = 0; i < pseudo.size(); i++) {
            System.out.printf("%s\t\t%d\n", pseudo.elementAt(i), ppos.elementAt(i));
        }
        System.out.println("\n-----Symbol Table-----\n");
        System.out.println("Name Counter Length R/A");
        for (int i = 0; i < symbolname.size(); i++) {
            System.out.printf("%s\t%d\t%d\t%s\n", symbolname.elementAt(i), symbolvalue.elementAt(i),
                    symbollength.elementAt(i), RA.elementAt(i));
        }
    }

    static int getIndex(String st[], String s) {
        for (int i = 0; i < st.length; i++)
            if (s.equals(st[i]))
                return i;
        return -1;
    }
}
