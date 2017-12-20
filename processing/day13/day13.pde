int TOTAL = 99;
int MAX_RANGE = 24;
int LARGEUR = 13;
int HAUTEUR = 20;
Layer[] layers = new Layer[TOTAL];

int picoseconds = 0;
int player = 0;


void setup() {
  parseFile();
}

void settings() {
  size((TOTAL + 2) * LARGEUR, (MAX_RANGE + 2) * HAUTEUR); // 100*10 / 26*20
}

void draw() {
  background(255);
  for (int i = 0; i < TOTAL; i++) {
    pushStyle();
    fill(0);
    textSize(6);
    text(str(i), i*LARGEUR + LARGEUR, 2*HAUTEUR/3);
    popStyle();
    Layer layer = layers[i];
    layer.display();
  }
  pushStyle();
  fill(255, 255, 0);
  ellipse((player+1)*LARGEUR + LARGEUR/2, HAUTEUR + HAUTEUR/2, LARGEUR/2, HAUTEUR/2);
  popStyle();
}

void mousePressed() {
  for (int i = 0; i < TOTAL; i++) {
    Layer layer = layers[i];
    layer.update();
  }
  player++;
}

void parseFile() {
  String[] lines;
  lines = loadStrings("input.txt");
  int currentLine = 0;
  for (int i = 0 ; i < 99; i++) {
    String[] data = split(lines[currentLine], ": ");
    int depth = int(data[0]);
    int range = int(data[1]);
    Layer layer  = new Layer(i, 0);
    if (i == depth) {
      layer = new Layer(depth, range);
      currentLine++;
    }
    layers[i] = layer;
  }
}