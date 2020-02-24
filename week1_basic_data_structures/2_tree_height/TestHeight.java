import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestHeight {

    public static void assertHeight(final int expHeight, final int[] parents) {
        assertEquals(expHeight, tree_height.height(parents, parents.length));
    }

    @Test
    public void test0() {
        final int[] parents = { -1 };
        assertEquals(0, tree_height.height(parents, parents.length));
    }

    @Test
    public void test1() {
        final int[] parents = { 4, -1, 4, 1, 1 };
        assertEquals(3, tree_height.height(parents, parents.length));
    }

    @Test
    public void test2() {
        final int[] parents = { -1, 0, 4, 0, 3 };
        assertEquals(4, tree_height.height(parents, parents.length));
    }

}
