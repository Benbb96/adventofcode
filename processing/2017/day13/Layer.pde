class Layer {
  int depth, range, scanner;
  boolean down;
  
  Layer(int depth, int range) {
    this.depth = depth;
    this.range = range;
    scanner = 0;
    down = true;
  }

  void reset() {
    scanner = 0;
    down = true;
  }

  void update() {
    if (down) {
      // Si le scanner descend
      if (scanner < range - 1) {
        scanner += 1;
      } else {
        scanner -= 1;
        down = false;
      }
    } else {
      // Si le scanner monte
      if (scanner > 0) {
        scanner -= 1;
      } else {
        scanner += 1;
        down = true;
      }
    }
  }
  
  void display() {
    for (int j = 0; j < range; j++) {
      if (scanner == j) {
        fill(255, 0, 0);
      } else {
        fill(255);
      }
      rect(depth*LARGEUR + LARGEUR, j*HAUTEUR + HAUTEUR, LARGEUR, HAUTEUR);
    }
  }
}