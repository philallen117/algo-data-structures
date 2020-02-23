import java.util.ArrayDeque;
import java.util.ArrayList;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

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
    public void testB0(){
        Request rq0 = new Request(0,1);
        ArrayDeque<Response> q = new ArrayDeque<Response>(0);
        Response rs0 = process_packages.processNext(0, rq0, q);
        assertEquals(true, rs0.dropped);
        assertEquals(-1, rs0.start_time);
    }

    @Test
    public void test01() {
        ArrayList<Request> reqs = new ArrayList<Request>(0);
        ArrayList<Response> resps = process_packages.processAll(999, reqs);
        assertEquals(0,     resps.size());
    }

    @Test
    public void test17() {
        int[] p = {0, 2, 1, 2, 2, 2, 3, 2, 4, 2, 5, 2};
        ArrayList<Request> reqs = fromInts(p);
        ArrayList<Response> resps = process_packages.processAll(2, reqs);
        assertEquals(0,     resps.get(0).start_time);
        assertEquals(2,     resps.get(1).start_time);
        assertEquals(4,     resps.get(2).start_time);
        assertEquals(6,     resps.get(3).start_time);
        assertEquals(8,     resps.get(4).start_time);
        assertEquals(-1,    resps.get(5).start_time);
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
