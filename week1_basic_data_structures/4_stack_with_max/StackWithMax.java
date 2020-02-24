import java.util.*;
import java.io.*;

public class StackWithMax {
    class FastScanner {
        StringTokenizer tok = new StringTokenizer("");
        BufferedReader in;

        FastScanner() {
            in = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() throws IOException {
            while (!tok.hasMoreElements())
                tok = new StringTokenizer(in.readLine());
            return tok.nextToken();
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }

    public class StackMaxInt {
        class Pair {
            public int elem;
            public int max;

            public Pair(int elem, int max) {
                this.elem = elem;
                this.max = max;
            }
        }

        public Stack<Pair> s = new Stack<Pair>();

        public boolean empty() {
            return s.empty();
        }

        public int max() {
            if (s.empty())
                return 0;
            return s.peek().max;
        }

        public void push(int i) {
            int max_below = max();
            s.push(new Pair(i, Math.max(max_below, i)));
        }

        public void pop() {
            s.pop();
        }
    }

    public void solve() throws IOException {
        FastScanner scanner = new FastScanner();
        int queries = scanner.nextInt();
        // Stack<Integer> stack = new Stack<Integer>();
        StackMaxInt stack = new StackMaxInt();
        for (int qi = 0; qi < queries; ++qi) {
            String operation = scanner.next();
            if ("push".equals(operation)) {
                int value = scanner.nextInt();
                stack.push(value);
            } else if ("pop".equals(operation)) {
                stack.pop();
            } else if ("max".equals(operation)) {
                // System.out.println(Collections.max(stack));
                System.out.println(stack.max());
            }
        }
    }

    static public void main(String[] args) throws IOException {
        new StackWithMax().solve();
    }
}
