import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import java.util.Stack;

public class TestMaxStack {
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

  @Test
  public void testX() {
    StackMaxInt s = new StackMaxInt();
    assertEquals(s.empty(), true);
    s.push(1);
    assertFalse(s.empty());
    s.push(5);
    assertEquals(5, s.max());
    s.push(3);
    assertEquals(5, s.max());
    s.push(6);
    assertEquals(6, s.max());
    s.pop();
    assertEquals(5, s.max());
    s.pop();
    s.pop();
    assertEquals(1, s.max());
  }

}
