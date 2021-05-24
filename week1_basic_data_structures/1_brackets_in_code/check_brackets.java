import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Iterator;
import java.util.Stack;

class Bracket {
    Bracket(char type, int position) {
        this.type = type;
        this.position = position;
    }

    boolean Match(char c) {
        if (this.type == '[' && c == ']')
            return true;
        if (this.type == '{' && c == '}')
            return true;
        if (this.type == '(' && c == ')')
            return true;
        return false;
    }

    boolean opening() {
        return type == '[' || type == '{' || type == '(';
    }

    char type;
    int position;
}

class check_brackets {
    public static int check(String text) {
        Stack<Bracket> opening_brackets_stack = new Stack<Bracket>();
        for (int position = 1; position <= text.length(); ++position) {
            // convert position to 0-index
            char next = text.charAt(position - 1);
            if (next == '(' || next == '[' || next == '{')
                opening_brackets_stack.push(new Bracket(next, position));
            if (next == ')' || next == ']' || next == '}') {
                if (opening_brackets_stack.empty())
                    return position;
                Bracket b = opening_brackets_stack.pop();
                if (!b.Match(next))
                    return position;
            }
        }
        if (opening_brackets_stack.empty())
            return 0;
        else {
            // Find first non-matching opening bracket.
            Iterator<Bracket> remaining = opening_brackets_stack.iterator();
            Bracket candidate = null;
            while (remaining.hasNext()) {
                candidate = remaining.next();
                if (candidate.opening())
                    break;
            }
            if (!candidate.opening())
                throw new AssertionError("bug - should be opening bracket");
            return candidate.position;
        }
    }

    public static void main(String[] args) throws IOException {
        InputStreamReader input_stream = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(input_stream);
        String text = reader.readLine();
        int res = check(text);
        if (res == 0)
            System.out.println("Success");
        else
            System.out.println(res);
    }
}
