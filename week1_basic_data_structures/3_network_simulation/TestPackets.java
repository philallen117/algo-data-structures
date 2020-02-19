import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.ArrayDeque;
import java.util.ArrayList;

public class TestPackets {
    public ArrayList<Request> fromInts(int[] p) {
        int psize = p.length;
        int lsize = psize / 2;
        ArrayList<Request> l = new ArrayList<Request>(lsize);
        for (int i = 0; i < psize; i += 2) {
            l.add(new Request(p[i], p[i + 1]));
        }
        return l;
    }

    @Test
    public void test0(){
        Request rq0 = new Request(0,1);
        ArrayDeque<Response> q = new ArrayDeque<Response>(0);
        Response rs0 = process_packages.processNext(0, rq0, q);
        assertEquals(true, rs0.dropped);
        assertEquals(-1, rs0.start_time);
    }

    @Test
    public void test18() {
        int[] p = {0, 1, 3, 1, 10, 1};
        ArrayList<Request> reqs = fromInts(p);
        ArrayList<Response> resps = process_packages.processAll(2, reqs);
        assertEquals(0,     resps.get(0).start_time);
        assertEquals(3,     resps.get(1).start_time);
        assertEquals(10,    resps.get(2).start_time);
    }
}
