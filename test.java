import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CalculatorTest {

    // Funcția pe care o testăm
    public int add(int a, int b) {
        return a + b;
    }

    // Testul pentru funcția add
    @Test
    public void testAdd() {
        CalculatorTest calculator = new CalculatorTest();
        int result = calculator.add(2, 3);
        // Verificăm dacă suma este corectă
        assertEquals(5, result, "Suma ar trebui să fie 5");
    }
}
