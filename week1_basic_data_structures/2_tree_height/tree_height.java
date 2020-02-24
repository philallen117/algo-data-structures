import java.util.*;
import java.io.*;

public class tree_height {
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

	public static int height(int parent[], int n) {
		int height[] = new int[n]; // assume init 0, so root is already correct
		for (int vertex = 0; vertex < n; vertex++) {
			if (height[vertex] > 0 || parent[vertex] == -1)
				continue; // known or root
			Stack<Integer> path = new Stack<Integer>();
			path.push(vertex);
			int pv = parent[vertex];
			while (pv != -1 && height[pv] > 0) { // not known
				path.push(pv);
				pv = parent[pv];
			}
			int pvHeight = height[pv];
			while (!path.isEmpty()) {
				pvHeight += 1;
				pv = path.pop();
				height[pv] = pvHeight;
			}
		}
		int maxHeight = 0;
		for (int h : height) {
			maxHeight = Math.max(maxHeight, h);
		}
		return maxHeight;
	}

	public class TreeHeight {
		int n;
		int parent[];

		void read() throws IOException {
			FastScanner in = new FastScanner();
			n = in.nextInt();
			parent = new int[n];
			for (int i = 0; i < n; i++) {
				parent[i] = in.nextInt();
			}
		}

		int computeHeight() {
			return height(parent, n);
		}
	}

	public void run() throws IOException {
		TreeHeight tree = new TreeHeight();
		tree.read();
		System.out.println(tree.computeHeight());
	}

	static public void main(String[] args) throws IOException {
		new Thread(null, new Runnable() {
			public void run() {
				try {
					new tree_height().run();
				} catch (IOException e) {
				}
			}
		}, "1", 1 << 26).start();
	}
}
