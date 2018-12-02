int TOTAL = 99;
int MAX_RANGE = 24;
int LARGEUR = 13;
int HAUTEUR = 20;
Layer[] layers = new Layer[TOTAL];

int picoseconds = 0;
int player;
int severity = 0;
int speed = 7;
int attempt = 0;

boolean pause = false;
boolean end = false;
boolean part2 = true;
boolean ready = true;


void setup() {
  parseFile();
  if (part2) {
    player = -1;
    attempt++; // First attempt
  } else {
    player = 0;
  }
  int delay = 0;
  while (delay < 3830340) {
    for (int i = 0; i < TOTAL; i++) {
    Layer layer = layers[i];
      layer.update();
    }
    delay++;
  }
}

void settings() {
  size((TOTAL + 2) * LARGEUR, (MAX_RANGE + 2) * HAUTEUR); // 100*10 / 26*20
}

void draw() {
  // Display the game
  background(255);
  pushStyle();
  fill(0);
  textSize(23);
  text("Picoseconds : " + str(picoseconds), 30, height -90);
  text("Attempt : " + str(attempt), 30, height -60);
  text("Damage : " + str(severity), 30, height -30);
  if (end) {
    textSize(30);
    text("The end !", width/2, height - 100);
  }
  popStyle();
  displayLayers();
  displayPlayer();
  
  // Move it all
  if (frameCount % speed == 0 && !pause && !end) {
    tick();
  }
}

void mousePressed() {
  tick();
}

void mouseWheel(MouseEvent event) {
  float e = event.getCount();
  if (speed > 1 && e < 0) {
    speed -= 3;
  } else if (speed <= 15 && e > 0) {
    speed += 3;
  }
}

void keyPressed() {
  if (key == 'r') {
    reset();
  } else if (key == 'p') {
    pause = !pause;
  }
}

void tick() {
  picoseconds++;
  // One tick of the game : layers' scanner move and the player too
  for (int i = 0; i < TOTAL; i++) {
    Layer layer = layers[i];
    layer.update();
  }
  if (!pause && ready) {
    player++;
  } else if (!ready) {
    if (picoseconds == attempt) {
      ready = true;
      speed = 7;
    }
  }
  if (player == TOTAL-1) {
    end = true;
  }
  checkIfPlayerCaught();
}

void checkIfPlayerCaught() {
  // Vérifie si le joueur est attrapé par un scanner
  if (player > 0 && layers[player].scanner == 0) {
    if (part2) {
      reset();
    } else {
      severity += player * layers[player].range;
    }
  }
}

void displayPlayer() {
  pushStyle();
  fill(255, 255, 0);
  ellipse((player+1)*LARGEUR + LARGEUR/2, HAUTEUR + HAUTEUR/2, LARGEUR/2, HAUTEUR/2);
  popStyle();
}

void displayLayers() {
  for (int i = 0; i < TOTAL; i++) {
    pushStyle();
    fill(0);
    textSize(6);
    text(str(i), i*LARGEUR + LARGEUR, 2*HAUTEUR/3);
    popStyle();
    Layer layer = layers[i];
    layer.display();
  }
}

void reset() {
  end = false;
  severity = 0;
  picoseconds = 0;
  for (int i = 0; i < TOTAL; i++) {
    Layer layer = layers[i];
    layer.reset();
  }
  
  if (part2) {
    ready = false;
    attempt++;
    player = -1;
    speed = 1;
  } else {
    player = 0;
  }
}

void parseFile() {
  // Parse the input file in order to create all the layers
  String[] lines;
  lines = loadStrings("input.txt");
  int currentLine = 0;
  for (int i = 0 ; i < TOTAL; i++) {
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