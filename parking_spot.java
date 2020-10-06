// https://app.codesignal.com/challenge/Nyoi9DSYrwENBkSM2

class parking_spot 
{ 
    public static void main(String args[]) 
    { 
		// System.out.println("Hello, World");
		int[] carDimensions = new int[]{2, 1};
		int[] luckySpot = new int[]{0, 1, 1, 1};
		
		int[][] parkingLot = new int[3][3];
		
		// int[] temp0 = new int[]{1,0,1,0,1,0};
		// int[] temp1 = new int[]{0,0,0,0,1,0};
		// int[] temp2 = new int[]{0,0,0,0,0,1};
		// int[] temp3 = new int[]{1,0,1,1,1,1};

		// int[] temp0 = new int[]{1,0,1,0,1,0};
		// int[] temp1 = new int[]{1,0,0,0,1,0};
		// int[] temp2 = new int[]{0,0,0,0,0,1};
		// int[] temp3 = new int[]{1,0,0,0,1,1};

		int[] temp0 = new int[]{1,0,1};
		int[] temp1 = new int[]{1,0,1};
		int[] temp2 = new int[]{1,1,1};

		parkingLot[0] = temp0;
		parkingLot[1] = temp1;
		parkingLot[2] = temp2;
		// parkingLot[3] = temp3;



		boolean result = parkingSpot(carDimensions, parkingLot, luckySpot);
		System.out.println(result);

	} 
	
	public static boolean parkingSpot(int[] carDimensions, int[][] parkingLot, int[] luckySpot) {
		boolean fits = true;
		boolean horizontal = false;
		if (carDimensions[0] > carDimensions[1]) {
			horizontal = true;
		}
		int startx = luckySpot[0]; // 1
		int starty = luckySpot[1]; // 1
		int endx = luckySpot[2]; // 2
		int endy = luckySpot[3]; // 3
		int maxx = parkingLot.length;
		int maxy = parkingLot[0].length;

		// System.out.println("max x: " + maxx + ", max y: " + maxy);

		// check whether everything in the parkingspot is a zero
		for (int row = startx; row <= endx; row++) {
			for (int column = starty; column <= endy; column++) {
				if (parkingLot[row][column] == 1) {
					fits = false;
				}
			}
		}

		if (horizontal) {
			// if horizontal then check everything before
			boolean horizontalSpace = true;
			for (int row = startx; row <= endx; row++) {
				for (int column = 0; column < starty; column++) {
					if (parkingLot[row][column] == 1) {
						horizontalSpace = false;
					}
				}
			}
			// if no space before then check space after
			if (!horizontalSpace) {
				for (int row = startx; row <= endx; row++) {
					for (int column = endy; column < maxy; column++) {
						if (parkingLot[row][column] == 1) {
							horizontalSpace = false;
						}
					}
				}
			}

			if (!horizontalSpace) {
				fits = false;
			}
		} else { // check vertical spaces
			// check vertical spaces before
			boolean verticalSpace = true;
			for (int row = 0; row < startx; row++) {
				for (int column = starty; column <= endy; column++) {
					if (parkingLot[row][column] == 1) {
						verticalSpace = false;
					}
				}
			}
			// if no space before then check space after
			if (!verticalSpace) {
				for (int row = endx; row < maxx; row++) {
					for (int column = starty; column <= endy; column++) {
						if (parkingLot[row][column] == 1) {
							verticalSpace = false;
						}
					}
				}
			}
			if (!verticalSpace) {
				fits = false;
			}
		}

		return fits;
	}
}