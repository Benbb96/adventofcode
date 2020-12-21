int size = 500;

class Cube {
  PVector position;
  Boolean state;
  
  Cube(PVector position, boolean state) {
    this.position = position;
    this.state = state;
  }
  
  void display() {
    pushMatrix();
    stroke(0);
    strokeWeight(5);
    if (state) {
      fill(200, 100, 155);
    } else {
      noFill();
    }
    // Draw the cube at its position
    translate(position.x * size, position.y * size, position.z * size);
    box(size/2);
    popMatrix();
  }
  
  boolean update(ArrayList<Cube> cubeList) {
    int countNeighbors = 0;
    for (int i = 0 ; i < cubeList.size(); i++) {
      Cube cube = cubeList.get(i);
      if (cube != this) {
        if (abs(cube.position.x - this.position.x) < 2 && abs(cube.position.y - this.position.y) < 2 && abs(cube.position.z - this.position.z) < 2) {
          if (cube.state) countNeighbors++;
        }
      }
    }
    
    boolean futurState = this.state;
    if (this.state) {
       if (countNeighbors < 2 || countNeighbors > 3) futurState = false;
    } else {
      if (countNeighbors == 3) futurState = true;
    }
    
    return futurState;
  }
}
