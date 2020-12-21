// Day 17 of the Advent of Code 2020
// https://adventofcode.com/2020/day/17


ArrayList<Cube> cubeList = new ArrayList<Cube>();  // My list of cubes
boolean[][][] grid = new boolean[100][100][100];

float a = 0, b = 0;  // Variable to make it rotate along the x and y axis

boolean save = false;  // Save the frames if true

float scale = 0.2;

void setup() {
  size(1120, 640, P3D);
  frameRate(1);
  parseInput("test");
}

void draw() {
  background(255);
  
  prepareCamera();
  
  ArrayList<Cube> futurCubeList = new ArrayList<Cube>();
  
  for (int i = 0 ; i < cubeList.size(); i++) {
    Cube cube = cubeList.get(i);
    if (frameCount < 6) {
      boolean futurState = cube.update(cubeList);  // Do the calculation to move the point
      futurCubeList.add(new Cube(cube.position, futurState));
    }
    cube.display();  // Draw the cube
  }
  cubeList = futurCubeList;
  
  if (save) {
    saveFrame("frames/###.gif");
  }
}

void parseInput(String filename) {
  // Retrieve each point from the input text
  String[] lines = loadStrings(filename + ".txt");
  int x = -1;
  int y = -1;
  int z = 0;
  for (int i = 0 ; i < lines.length; i++) {
    y = 0;
    for (int j = 0 ; j < lines[i].length(); j++) {
      char current = lines[i].charAt(j);
      boolean state = false;
      if (current == '#') {
        state = true;
      }
      PVector position = new PVector(x, y, z);
      grid[x+50][y+50][z+50] = true;
      Cube cube = new Cube(position, state);
      cubeList.add(cube);
      y++;
    }
    x++;
  }
  //println(grid);
}

void drawAxis() {
  // Add the three lines corresponding of the x (red), y (green) and z (blue) axis
  strokeWeight(1);
  stroke(255, 0, 0);
  line(-200, 0, 0, 200, 0, 0);
  stroke(0, 255, 0);
  line(0, -200, 0, 0, 200, 0);
  stroke(0, 0, 255);
  line(0, 0, -200, 0, 0, 200);
}

void prepareCamera() {
  // Translate to the center of the view
  translate(width/2, height/2, 0);
  
  // Make a nice rotation
  rotateX(a % (2 * PI));
  a -= 0.2;
  rotateY(b % (2 * PI));
  b += 0.5;
  rotateZ(5*PI/4);
  
  drawAxis();
  
  // Gently zoom out
  scale *= 0.985;
  scale(scale);
}
