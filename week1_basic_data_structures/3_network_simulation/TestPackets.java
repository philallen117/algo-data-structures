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
    
    public ArrayList<Response> processAll(int size, ArrayList<Request> reqs) {
        ArrayList<Response> resps = new ArrayList<Response>(size);
        ArrayDeque<Response> q = new ArrayDeque<Response>(size); // buffer
        for (Request req : reqs) {
            Response resp = process_packages.processNext(size, req, q);
            resps.add(resp);
        }
        return resps;
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
    public void testB1(){
        Request rq0 = new Request(3,1);
        ArrayDeque<Response> q = new ArrayDeque<Response>(0);
        Response rs0 = process_packages.processNext(1, rq0, q);
        assertEquals(false, rs0.dropped);
        assertEquals(3, rs0.start_time);
    }

    @Test
    public void testB18() {
//        int[] p = {0, 1, 3, 1, 10, 1};
//        ArrayList<Request> reqs = fromInts(p);
        ArrayDeque<Response> q = new ArrayDeque<Response>(0);
        ArrayList<Request> reqs = new ArrayList<Request>();
        Request rq0 = new Request(0, 1);
        Response rs0 = process_packages.processNext(2, rq0, q);
        assertEquals(0,     rs0.start_time);
        Request rq1 = new Request(3, 1);
        Response rs1 = process_packages.processNext(2, rq1, q);
        assertEquals(3,     rs1.start_time);
        Request rq2 = new Request(10, 1);
        Response rs2 = process_packages.processNext(2, rq2, q);
        assertEquals(10,    rs2.start_time);
    } 
    
    @Test
    public void test01() {
        ArrayList<Request> reqs = new ArrayList<Request>(0);
        ArrayList<Response> resps = processAll(999, reqs);
        assertEquals(0,     resps.size());
    }

    @Test
    public void test17() {
        int[] p = {0, 2, 1, 2, 2, 2, 3, 2, 4, 2, 5, 2};
        ArrayList<Request> reqs = fromInts(p);
        ArrayList<Response> resps = processAll(3, reqs);
        assertEquals(0,     resps.get(0).start_time);
        assertEquals("here!!", 2,     resps.get(1).start_time);
        assertEquals(4,     resps.get(2).start_time);
        assertEquals(6,     resps.get(3).start_time);
        assertEquals(8,     resps.get(4).start_time);
        assertEquals(-1,    resps.get(5).start_time);
    }

    @Test
    public void test18() {
        int[] p = {0, 1, 3, 1, 10, 1};
        ArrayList<Request> reqs = fromInts(p);
        ArrayList<Response> resps = processAll(2, reqs);
        assertEquals(0,     resps.get(0).start_time);
        assertEquals(3,     resps.get(1).start_time);
        assertEquals("there!!", 10,    resps.get(2).start_time);
    }
}
