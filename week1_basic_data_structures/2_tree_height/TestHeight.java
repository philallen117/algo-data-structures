import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestHeight {

    @Test
    public void test0() {
        assertEquals(0, 0);
    }

     public static void assertHeight(int expHeight, int[] parents) {
         assertEquals(expHeight, tree_height.height(parents, parents.length));
     }

     @Test
     public void test1() {
         int [] parents = {-1};
         assertHeight(0, parents);
     }
}
