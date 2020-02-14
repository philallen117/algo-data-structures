import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
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

    char type;
    int position;
}

class check_brackets {
    public static int check(String text) {
        Stack<Bracket> opening_brackets_stack = new Stack<Bracket>();
        for (int position = 0; position < text.length(); ++position) {
            char next = text.charAt(position);
            if (next == '(' || next == '[' || next == '{')
                opening_brackets_stack.push(new Bracket(next, position + 1));
            if (next == ')' || next == ']' || next == '}') {
                if (opening_brackets_stack.empty()) return position + 1;
                Bracket b = opening_brackets_stack.pop();
                if (!b.Match(next)) return b.position;
            }
        }
        if (opening_brackets_stack.empty())
            return 0;
        else
            return opening_brackets_stack.pop().position;
    }

    public static void main(String[] args) throws IOException {
        InputStreamReader input_stream = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(input_stream);
        String text = reader.readLine();
        int res = check(text);
        if (res==0)
            System.out.println("Success");
        else
        System.out.println(res);
    }
}
