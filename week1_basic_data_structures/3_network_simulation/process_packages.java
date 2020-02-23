import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Scanner;

class Request {
    public int arrival_time;
    public int process_time;
    
    public Request(int arrival_time, int process_time) {
        this.arrival_time = arrival_time;
        this.process_time = process_time;
    }
}

class Response {
    public Response(boolean dropped, int start_time, int finish_time) {
        this.dropped = dropped;
        this.start_time = start_time;
        this.finish_time = finish_time;
    }
    
    public boolean dropped;
    public int start_time;
    public int finish_time;
}

class Buffer {
    private int size;
    private ArrayDeque<Response> q;
    
    public Buffer(int size) {
        this.size = size;
        this.q = new ArrayDeque<Response>(size);
    }
    
    public Response process(Request request) {
        // write your code here
        return process_packages.processNext(size, request, q);
    }
}

class process_packages {
    
    // Mutates requestQueue to add new arrival, if within capacity
    static Response processNext(int size, Request req, ArrayDeque<Response> q) {
        int arrival_time = req.arrival_time;
        while (!q.isEmpty() && q.peekLast().start_time > arrival_time) q.removeLast();
        if (q.size() >= size) return new Response(true, -1, 0);
        int next_available_time = q.isEmpty() ? -1 : q.peekFirst().finish_time;
        int start_time = Math.max(arrival_time, next_available_time);
        int finish_time = start_time + req.process_time;
        return new Response(false, start_time, finish_time);
    }
    
    static ArrayList<Response> processAll(int size, ArrayList<Request> reqs) {
        ArrayList<Response> resps = new ArrayList<Response>(size);
        ArrayDeque<Response> q = new ArrayDeque<Response>(size);
        for (Request req : reqs) {
            Response resp = processNext(size, req, q);
            resps.add(resp);
        }
        return resps;
    }
    
    private static ArrayList<Request> ReadQueries(Scanner scanner) {
        int requests_count = scanner.nextInt();
        ArrayList<Request> requests = new ArrayList<Request>();
        for (int i = 0; i < requests_count; ++i) {
            int arrival_time = scanner.nextInt();
            int process_time = scanner.nextInt();
            requests.add(new Request(arrival_time, process_time));
        }
        return requests;
    }
    
    private static ArrayList<Response> ProcessRequests(ArrayList<Request> requests, Buffer buffer) {
        ArrayList<Response> responses = new ArrayList<Response>();
        for (int i = 0; i < requests.size(); ++i) {
            responses.add(buffer.process(requests.get(i)));
        }
        return responses;
    }
    
    private static void PrintResponses(ArrayList<Response> responses) {
        for (int i = 0; i < responses.size(); ++i) {
            Response response = responses.get(i);
            if (response.dropped) {
                System.out.println(-1);
            } else {
                System.out.println(response.start_time);
            }
        }
    }
    
    public static void main(String[] args     ) {
        Scanner scanner = new Scanner(System.in);
        int buffer_max_size = scanner.nextInt();
        Buffer buffer = new Buffer(buffer_max_size);
        ArrayList<Request> requests = ReadQueries(scanner);
        ArrayList<Response> responses = ProcessRequests(requests, buffer);
        PrintResponses(responses);
    }
}
