public class rotate_image {
	public static void main(String args[]) { 
		// run tests here
	}

	public static int[][] rotateImage(int[][] a) {
		int size = a.length; 
		int[][] result = new int[size][size];
		
		for(int row = 0; row < size; row++){
			int new_row = size - row - 1;
			for(int column = 0; column < size; column++){
				// System.out.println("Inserted: " + a[row][column] + " into " + " (" + column + ", " + new_row + ")");
				result[column][new_row] = a[row][column];
			}
		}
		
		return result;
	}
}
